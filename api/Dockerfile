FROM python:3.9-slim

COPY ./src /app/src/
COPY ./src/requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port", "80"]