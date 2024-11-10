FROM python:3.9

# ... 既存のコード ...
WORKDIR /app

COPY requirements.txt search.py index.html ./
COPY ask_models.json /app/models/

EXPOSE 3000

CMD ["bash", "-c", "pip install -r requirements.txt && python search.py"]
