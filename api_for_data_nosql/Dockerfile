FROM python:3.11-slim-buster
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python3", "cache_api/api.py"]