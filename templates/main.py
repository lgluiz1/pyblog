import streamlit as st
import requests

BASE_URL = "https://736b-191-241-65-200.ngrok-free.app"
API_URL = f"{BASE_URL}/api/"

st.title("Login no Blog")

# Formulário de login
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    login_url = f"{BASE_URL}/api-token-auth/"
    response = requests.post(login_url, data={"username": username, "password": password})

    if response.status_code == 200:
        token = response.json().get("token")
        st.success("Login realizado com sucesso!")

        # Armazena o token na sessão
        st.session_state["token"] = token

    else:
        st.error("Usuário ou senha inválidos.")

# Se logado, exibe formulário para criar post
if "token" in st.session_state:
    st.title("Criar novo post")

    title = st.text_input("Título do Post")
    text = st.text_area("Conteúdo do Post")

    if st.button("Publicar"):
        headers = {
            "Authorization": f"Token {st.session_state['token']}"
        }
        response = requests.post(f'{API_URL}posts/', headers=headers, data={"title": title, "text": text})
        if response.status_code == 201:
            st.success("Post criado com sucesso!")
        else:
            st.error(f"Erro ao criar post: {response.status_code}")

    st.title("Listagem de Posts")

    # Listagem de posts
    response = requests.get(f'{API_URL}posts/')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            st.write(f"{post['title']} - {post['text']}")