# app/context_processors.py

from blog.models import Category, Tags  # ajuste conforme seus modelos

def categorias_e_tags(request):
    categorias = Category.objects.all()
    tags = Tags.objects.all()
    return {
        'categorias_base': categorias,
        'tags_base': tags
    }
