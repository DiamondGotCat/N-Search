
<img width="1698" alt="Screenshot" src="https://github.com/user-attachments/assets/66b4da36-edd1-4fb2-a86b-d48c4beb5e31">

# N-Search

## Features
- [x] Modern Design
- [x] Ranking with AI
- [x] Ask AI
- [x] Selectable LLM

## Structure

### Search
1. Search Button Clicked
2. Search on MySQL
3. Search on DuckDuckGo
4. Ranking Result with `all-MiniLM-L6-v2`
5. Show

### Ask AI
1. Query has Sent to Server
2. Generate Answer using `llama-cpp-python`
3. Show

## Search Source
- DuckDuckGo
- MySQL in Docker (Manually crawl)

## How to Use
1. Install Docker
2. Install N-Search with Docker-compose Command (`docker-compose up -d`)
3. Access [localhost:3000](http://localhost:3000/)
