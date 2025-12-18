import streamlit as st
import requests
from loguru import logger
from sys import stderr

logger.add(stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("logs/streamlit.log")

st.header("Frontend")

with st.form("my_form"):
    st.write("Saisissez un nombre")
    number = st.int("Saisissez un nombre.")
    submitted = st.form_submit_button("Envoyer")

    if submitted:
        try:
            response = requests.post("http://127.0.0.1:80/calcul/", json={"number": number})
            response.raise_for_status()
            json = response.json()

            st.write(f"Résultat : {json}")
        except requests.exceptions.HTTPError as e:
            st.error(f"Erreur HTTP : {e}")
            logger.error(f"Erreur HTTP : {e}")
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {e}")
            logger.error(f"Erreur de connexion à l'API : {e}")
        except Exception as e:
            st.error(f"Erreur lors de l'analyse: {e}")

