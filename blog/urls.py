from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/<slug:slug>/', views.posts_por_categoria, name='posts_por_categoria'),
    path('tags/<slug:slug>/', views.posts_por_tags, name='posts_por_tags'),
    path('posts/<slug:slug>/', views.posts_por_postagem, name='posts_por_postagem'),
    path('post/<slug:slug>/', views.detalhe_post, name='posts_detalhe'),
    path('login/success/', views.login_success, name='login_success'),
    path("login/github-direct/", views.github_login_redirect, name="github-direct-login"),
    

    path('buscar/', views.buscar_posts, name='buscar_posts'),

    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
]

# Servir arquivos de mídia no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)