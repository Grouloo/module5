FROM python:3.12.12-slim-trixie

WORKDIR /app

COPY . .

# Installation des dépendances
RUN pip install -r requirements.txt

EXPOSE 8080

RUN cd frontend

CMD ["streamlit", "run", "sentiment_streamlit.py", "--server.port 8080", "--server.address 0.0.0.0"]