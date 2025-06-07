import requests
from dotenv import load_dotenv
import os

load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}

def resumir_texto(texto):
    print(texto)
    payload = {"inputs": texto}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        resumo = response.json()
        if isinstance(resumo, list) and resumo:
            return resumo[0]['summary_text']
    return None
