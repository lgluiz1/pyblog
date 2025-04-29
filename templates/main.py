import streamlit as st
import requests

API_URL = "http://localhost:8000/api/"
TOKEN = "a45215a6fced4afd218e72bdae1b7a181342eb59"  # Ou carregue dinamicamente

headers = {
    "Authorization": f"Token {TOKEN}"
}

st.title("Criar novo post no Blog")

title = st.text_input("Título do Post")
text = st.text_area("Conteúdo do Post")

if st.button("Publicar"):
    if title and text:
        url = "posts/"
        response = requests.post(f'{API_URL}{url}', headers=headers, data={"title": title, "text": text})
        if response.status_code == 201:
            st.success("Post criado com sucesso!")
        else:
            st.error(f"Erro ao criar post: {response.status_code}")
    else:
        st.warning("Preencha todos os campos.")