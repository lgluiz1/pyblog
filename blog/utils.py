import requests
from dotenv import load_dotenv
from django.core.mail import send_mail
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


def notificar_novo_post(post):
    from .models import Notification
    from django.contrib.auth.models import User

    for user in User.objects.exclude(id=post.author.id):
        Notification.objects.create(
            recipient=user,
            message=f'Novo post: {post.title}',
            link=f'/post/{post.id}/'
        )
        send_mail(
            subject='Novo post no blog',
            message=f'Um novo post foi publicado: {post.title}',
            from_email='legalhints@gmail.com',
            recipient_list=[user.email],
        )

def notificar_comentario(comment):
    from .models import Notification

    post = comment.post

    if comment.writer != post.author:
        Notification.objects.create(
            recipient=post.author,
            message=f'{comment.writer.username} comentou no seu post "{post.title}"',
            link=f'/post/{post.id}/'
        )

    if comment.parent and comment.parent.writer != comment.writer:
        Notification.objects.create(
            recipient=comment.parent.writer,
            message=f'{comment.writer.username} respondeu seu comentário no post "{post.title}"',
            link=f'/post/{post.id}/#comment-{comment.id}'
        )