FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0", "flaskr:create_app()"]
