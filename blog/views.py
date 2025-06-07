from django.shortcuts import get_object_or_404, render
from .models import Post , Category , Comment, Image, Review, Tags
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from allauth.socialaccount.models import SocialAccount


def posts_por_categoria(request, slug):
    categoria = get_object_or_404(Category, slug=slug)
    posts = categoria.posts.all()  # usando related_name='posts'
    return render(request, 'categorias/posts_por_categoria.html', {'categoria': categoria, 'posts': posts})

def posts_por_tags(request, slug):
    tags = get_object_or_404(Tags, slug=slug)
    posts = tags.posts.all()  # usando related_name='posts'
    return render(request, 'tags/posts_por_tags.html', {'tags': tags, 'posts': posts})

def posts_por_postagem(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts_relacionados = Post.objects.filter(category=post.category).exclude(id=post.id)[:5]
    return render(request, 'postagem/pagina_da_postagem.html', {'post': post, 'relacionados': posts_relacionados})

def buscar_posts(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    return render(request, 'postagem/busca.html', {
        'query': query,
        'resultados': resultados
    })



def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    post.autor = post.writer

    # Tenta pegar dados da conta GitHub (via django-allauth)
    try:
        social_account = SocialAccount.objects.get(user=post.writer, provider='github')
        extra_data = social_account.extra_data
        post.autor.github_avatar = extra_data.get("avatar_url")
        post.autor.github_url = extra_data.get("html_url")
        post.autor.github_bio = extra_data.get("bio")
        post.autor.github_name = extra_data.get("name")
    except SocialAccount.DoesNotExist:
        post.autor.github_avatar = None
        post.autor.github_url = None
        post.autor.github_bio = None
        post.autor.github_name = post.writer.username

    return render(request, 'postagem/detalhe.html', {
        'post': post,
        'comments': comments,
    })




def index(request):
    comments = Comment.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            'index/partials/posts_paginados.html',
            {'page_obj': page_obj, 'comment': comments},
            request=request
        )
        return JsonResponse({'html': html})

    context = {
        'page_obj': page_obj,
        'comment': comments,
    }
    return render(request, 'index/index.html', context)
