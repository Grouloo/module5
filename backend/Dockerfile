FROM python:3.12.12-slim-trixie

WORKDIR /app

COPY . .

# Installation des dépendances
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app/backend

EXPOSE 8000

CMD ["uvicorn main:app", "--host 0.0.0.0", "--port 8000"]