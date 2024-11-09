from flask import Flask, request, jsonify, send_from_directory, make_response
import mysql.connector
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
from flask_cors import CORS
import os
from transformers import pipeline
import itertools
import torch
import requests
from bs4 import BeautifulSoup
import re
from llama_cpp import Llama
from duckduckgo_search import DDGS as ddg

ask_models = {
    "llama3.2-3b-instruct": {
        "path": "/app/llama3.2-3b.gguf",
        "url": "https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf"
    }
}
ranking_model_name = "sentence-transformers/all-MiniLM-L6-v2"

KamuJpModern().modernLogging(process_name="Ask Models").log(list(ask_models.keys()).join("\n"), "INFO")
KamuJpModern().modernLogging(process_name="Ranking Model").log(ranking_model_name, "INFO")

import argparse
import requests
import os
import time
from KamuJpModern import KamuJpModern

class Downloader:
    ONE_MB = 1024 * 1024

    def __init__(self, title):
        self.total_downloaded = 0
        self.progress_bar = KamuJpModern().modernProgressBar(
            total=0,
            process_name=title,
            process_color=32
        )
        self.start_time = time.time()
        self.logger = KamuJpModern().modernLogging(process_name="Downloader")

    def get_file_size(self, url):
        try:
            response = requests.head(url, allow_redirects=True)
            response.raise_for_status()
            file_size = int(response.headers.get('Content-Length', 0))
            if file_size == 0:
                raise ValueError("Content-Length is zero or not provided.")
            return file_size
        except (requests.RequestException, ValueError):
            response = requests.get(url, stream=True)
            response.raise_for_status()
            file_size = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file_size += len(chunk)
            return file_size

    def on_unit_downloaded(self, bytes_downloaded):
        elapsed_time = time.time() - self.start_time
        total_downloaded_mb = self.total_downloaded / self.ONE_MB
        elapsed_time_formatted = time.strftime("%H hours %M minutes %S seconds", time.gmtime(elapsed_time))
        log_message = f"{total_downloaded_mb:.2f} MB downloaded in {elapsed_time_formatted}"
        self.progress_bar.logging(log_message)

    def download_file(self, url, output_path):
        file_size = self.get_file_size(url)
        if file_size == 0:
            print("Failed to get file size.")
            return
        unit_multiplier = self.ONE_MB
        total_units = file_size / unit_multiplier
        self.progress_bar.total = total_units
        self.progress_bar.start()
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error occurred during download: {e}")
            return
        downloaded = 0
        self.total_downloaded = 0 
        self.start_time = time.time()
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    chunk_size = len(chunk)
                    downloaded += chunk_size
                    self.total_downloaded += chunk_size
                    self.on_unit_downloaded(downloaded)
                    self.progress_bar.update(downloaded / unit_multiplier)
                    downloaded = 0
            if downloaded > 0:
                self.on_unit_downloaded(downloaded)
        self.progress_bar.finish()

def isExistLLMModel(model_name):
    return os.path.exists(ask_models[model_name]["path"])

def downloadLLMModel(model_name):
    downloader = Downloader(title="Downloading " + model_name)
    downloader.download_file(ask_models[model_name]["url"], ask_models[model_name]["path"])

app = Flask(__name__)
CORS(app)

# データベース接続設定
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',  # Docker内のホスト名
    'database': 'search_db',
    'charset': 'utf8mb4'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Initialize HuggingFace embeddings for document ranking
embedding_model = HuggingFaceEmbeddings(model_name=ranking_model_name)

# Initialize LLM for Ask AI feature
llm = pipeline(
    "text-generation",
    model="gpt2",
    device=0 if torch.cuda.is_available() else -1
)

ask_llms = {}
for model_name in ask_models:
    if not isExistLLMModel(model_name):
        KamuJpModern().modernLogging(process_name="Download LLM Model").log(f"Downloading {model_name}...", "INFO")
        downloadLLMModel(model_name)
    ask_llms[model_name] = Llama(model_path=ask_models[model_name]["path"])
    KamuJpModern().modernLogging(process_name="Set LLM Model").log(f"Setted {model_name}.", "INFO")

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/search-api/', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        KamuJpModern().modernLogging(process_name="Search API").log("Need query!", "ERROR")
        return jsonify({'error': 'Need query!'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, title, url, description FROM documents")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Perform DuckDuckGo search
    ddg_results = ddg().text(query, max_results=10)
    for result in ddg_results:
        results.append({
            'id': None,
            'title': result['title'],
            'url': result['href'],
            'description': result['body'],
            'similarity': None
        })
    
    if not results:
        return jsonify({'results': []})

    KamuJpModern().modernLogging(process_name="Search API").log(results.join("\n"), "INFO")

    def flatten_embeddings(embedding):
        if isinstance(embedding[0], list):
            return list(itertools.chain.from_iterable(itertools.chain.from_iterable(embedding)))
        return embedding

    query_embedding = flatten_embeddings(embedding_model.embed_query(query))
    document_embeddings = [
        (
            doc,
            flatten_embeddings(
                embedding_model.embed_query(doc['title'] + ' ' + doc['description'])
            )
        ) for doc in results
    ]

    def cosine_similarity(vec1, vec2):
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    threshold = 0.5
    relevant_docs = []
    for doc, embedding in document_embeddings:
        similarity = cosine_similarity(query_embedding, embedding)
        if similarity >= threshold:
            doc['similarity'] = similarity
            relevant_docs.append(doc)

    sorted_docs = sorted(relevant_docs, key=lambda x: x['similarity'], reverse=True)

    KamuJpModern().modernLogging(process_name="Search API").log(sorted_docs.join("\n"), "INFO")
    return jsonify({'results': sorted_docs})

@app.route('/models', methods=['GET'])
def get_models():
    KamuJpModern().modernLogging(process_name="Get Models").log(list(ask_models.keys()), "INFO")
    return jsonify(list(ask_models.keys()))

@app.route('/ask-ai', methods=['POST'])
def ask_ai():
    KamuJpModern().modernLogging(process_name="Ask AI").log("Asked!", "INFO")

    data = request.json
    query = data.get('query')
    model_name = data.get('model', 'llama3.1-8b-instruct')

    KamuJpModern().modernLogging(process_name="Ask AI").log(f"Query: {query}", "INFO")

    if not query:
        KamuJpModern().modernLogging(process_name="Ask AI").log("Need query!", "ERROR")
        return jsonify({'error': 'Need query!'}), 400

    try:
        response = ask_llms[model_name](query, max_tokens=8192)
        answer = response['choices'][0]['text'].split("[/assistant]")[0].split("[user]")[0].split("[/user]")[0].split("[inst]")[0].split("[/inst]")[0]
        KamuJpModern().modernLogging(process_name="Ask AI").log(f"AI response: {answer}", "INFO")
        return jsonify({'response': answer})
    except Exception as e:
        KamuJpModern().modernLogging(process_name="Ask AI").log(f'AI response failed: {str(e)}', "ERROR")
        return jsonify({'error': f'AI response failed: {str(e)}'}), 500

@app.route('/crawl-api/', methods=['POST', 'OPTIONS'])
def crawl():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response

    data = request.json
    url = data.get('url')
    if not url:
        KamuJpModern().modernLogging(process_name="Crawl API").log("Need URL!", "ERROR")
        return jsonify({'error': 'Need URL!'}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        description_tag = soup.find('meta', attrs={'name': 'description'})
        description = description_tag['content'] if description_tag else 'No Description'

        language = 'ja' if re.search('[\u3040-\u30ff\u4e00-\u9fff]', title + description) else 'en'
    except Exception as e:
        KamuJpModern().modernLogging(process_name="Crawl API").log(f'Failed to get data from URL: {str(e)}', "ERROR")
        return jsonify({'error': f'Failed to get data from URL: {str(e)}'}), 500

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO documents (title, url, description, language) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, url, description, language))
        conn.commit()
    except mysql.connector.IntegrityError:
        KamuJpModern().modernLogging(process_name="Crawl API").log("This URL already exists.", "ERROR")
        return jsonify({'error': 'This URL already exists.'}), 400
    except Exception as e:
        KamuJpModern().modernLogging(process_name="Crawl API").log(f'Failed to insert data: {str(e)}', "ERROR")
        return jsonify({'error': f'Failed to insert data: {str(e)}'}), 500
    finally:
        cursor.close()
        conn.close()

    KamuJpModern().modernLogging(process_name="Crawl API").log("Document added: " + title, "INFO")
    return jsonify({'status': 'Document added.'}), 201

if __name__ == '__main__':
    KamuJpModern().modernLogging(process_name="Server").log("Server started.", "INFO")
    app.run(host='0.0.0.0', port=3000)
