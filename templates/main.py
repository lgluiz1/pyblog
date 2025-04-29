import streamlit as st
import requests

BASE_URL = "https://736b-191-241-65-200.ngrok-free.app"
API_URL = f"{BASE_URL}/api/"

def show_post():
    st.title("Postagens do Blog")

    response = requests.get(f"{API_URL}posts/")
    posts = response.json()

    for post in posts:
        st.write(post["title"])
        st.write(post["text"])
        st.write("---")

    st.session_state["page"] = "login"

def show_login():
    st.title("Login no Blog")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        login_url = f"{BASE_URL}/api-token-auth/"
        response = requests.post(login_url, data={"username": username, "password": password})

        if response.status_code == 200:
            token = response.json().get("token")
            st.session_state["token"] = token
            st.session_state["page"] = "create_post"
            st.experimental_rerun( )
        else:
            st.error("Usuário ou senha inválidos.")

def show_create_post():
    st.title("Criar novo post no Blog")

    title = st.text_input("Título do Post")
    text = st.text_area("Conteúdo do Post")

    headers = {"Authorization": f"Token {st.session_state['token']}"}

    if st.button("Publicar"):
        if title and text:
            response = requests.post(
                f'{API_URL}posts/',
                headers=headers,
                data={"title": title, "text": text}
            )
            if response.status_code == 201:
                st.success("Post criado com sucesso!")
            else:
                st.error(f"Erro ao criar post: {response.status_code}")
        else:
            st.warning("Preencha todos os campos.")

# Inicialização de estado
if "token" not in st.session_state:
    st.session_state["token"] = None
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# Navegação condicional
if st.session_state["token"] and st.session_state["page"] == "create_post":
    show_create_post()
else:
    show_login()
