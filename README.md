# Blog com Django e Streamlit

## Descrição
Este projeto é um blog desenvolvido com Django no backend e Streamlit no frontend. O objetivo é criar um blog onde o autor pode postar artigos sobre Django e Python, com páginas para visualização, login e criação de postagens.

## Funcionalidades
- **Página Inicial**: Exibe todas as postagens do blog, avaliações e menu de navegação.
- **Página de Login**: Permite acesso apenas a usuários autorizados.
- **Página de Criação de Postagem**: Formulário para criar novas postagens.
- **Página do Artigo**: Página dinâmica para cada postagem, exibindo avaliações e comentários.

## Tecnologias Utilizadas
- **Backend**: Django
- **Frontend**: Streamlit
- **API**: Django REST Framework
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)

## Estrutura do Projeto
- **Django**:
  - `models.py`: Define os modelos para postagens, comentários e avaliações.
  - `views.py`: Define as views para criar, listar e detalhar postagens.
  - `urls.py`: Define os endpoints da API.
- **Streamlit**:
  - `app.py`: Define a interface do usuário e faz chamadas à API do Django.

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/lgluiz1/blogproject.git
   cd blogproject
   ```
   
## Configure o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
 ```

## Instale as dependências:
```bash
pip install -r requirements.txt
 ```

## Configure o Django:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
 ```

## Execute o Streamlit:
```bash
streamlit run app.py
 ```

## Hospedagem
- Frontend: Streamlit Community Cloud
- Backend: Heroku
- Contribuição

Sinta-se à vontade para contribuir com o projeto. Abra uma issue ou envie um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
Para dúvidas ou sugestões, entre em contato pelo email: lgluiz2536@gmail.com
