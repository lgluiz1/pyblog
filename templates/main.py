import streamlit as st
import requests

BASE_URL = "https://736b-191-241-65-200.ngrok-free.app"
API_URL = f"{BASE_URL}/api/"

def show_post():
    st.title("Postagens do Blog")

    # Recupera os posts
    response = requests.get(f"{API_URL}posts/")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            st.write(post["title"])
            st.write(post["text"])
            st.write("---")
    else:
        st.error(f"Erro ao carregar posts: {response.status_code}")

def show_login():
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        login_url = f"{BASE_URL}/api-token-auth/"
        response = requests.post(login_url, data={"username": username, "password": password})

        if response.status_code == 200:
            token = response.json().get("token")
            st.session_state["token"] = token
            st.session_state["page"] = "create_post"
            st.experimental_rerun()  # Recarrega a página para navegar para a criação de post
        else:
            st.error("Usuário ou senha inválidos.")

def show_create_post():
    st.title("Criar novo post no Blog")

    title = st.text_input("Título do Post")
    img = st.file_uploader("Imagem do Post", type=["png", "jpg", "jpeg"])
    text = st.text_area("Conteúdo do Post")

    headers = {"Authorization": f"Token {st.session_state['token']}"}

    if st.button("Publicar"):
        if title and text:
            # Criação do post
            post_response = requests.post(
                f'{API_URL}posts/',
                headers=headers,
                data={"title": title, "text": text}
            )

            if post_response.status_code == 201:
                st.success("Post criado com sucesso!")

                # Enviar imagem (se houver)
                if img:
                    files = {'image': (img.name, img, img.type)}  # Corrigido para enviar como 'files'
                    image_response = requests.post(
                        f'{API_URL}images/',
                        headers=headers,
                        files=files
                    )

                    if image_response.status_code == 201:
                        st.success("Imagem enviada com sucesso!")
                    else:
                        st.error(f"Erro ao enviar imagem: {image_response.status_code} - {image_response.text}")
            else:
                st.error(f"Erro ao criar post: {post_response.status_code}")
        else:
            st.warning("Preencha todos os campos.")

# Função para exibir categorias na barra lateral
def show_categories():
    categories = ["Categoria 1", "Categoria 2", "Categoria 3"]  # Exemplos de categorias
    selected_category = st.sidebar.selectbox("Escolha uma categoria", categories)
    st.sidebar.write(f"Você escolheu: {selected_category}")

# Configuração da página e navegação
def app():
    st.set_page_config(layout="wide")  # Usando layout "wide" para mais espaço
    show_categories()  # Exibe as categorias no menu lateral
    
    # Menu superior para login
    if "token" not in st.session_state:
        st.session_state["token"] = None
    if "page" not in st.session_state:
        st.session_state["page"] = "login"
    
    if st.session_state["token"]:
        # Exibir postagens ou criar post
        if st.session_state["page"] == "create_post":
            show_create_post()
        else:
            show_post()  # Exibe postagens do blog
    else:
        show_login()  # Exibe o formulário de login no blog

# Inicializa a aplicação
if __name__ == "__main__":
    app()
