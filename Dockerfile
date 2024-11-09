FROM python:3.9

WORKDIR /app

COPY requirements.txt search.py index.html ./

EXPOSE 3000
EXPOSE 3001

CMD ["bash", "-c", "pip install -r requirements.txt && python search.py"]