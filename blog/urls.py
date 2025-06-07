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

    path('buscar/', views.buscar_posts, name='buscar_posts'),
]

# Servir arquivos de mídia no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)