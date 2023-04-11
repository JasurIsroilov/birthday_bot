FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app/bd_bot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

#There should run celery worker
CMD ["celery", "-A", "mycelery", "beat"]
