from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.db.models import Count
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import resumir_texto
from django.utils.html import strip_tags
import logging
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icons_class_fontawesome = models.CharField(max_length=100 , blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
class Tags(models.Model):    
    tag = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.tag

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Post(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags, blank=True, related_name='posts')
    slug = models.SlugField(unique=True, blank=True, null=True)

    # IA
    short_title = models.CharField(max_length=50, blank=True)
    preview_summary = models.TextField(blank=True)

    

    def save(self, *args, **kwargs):
            logger = logging.getLogger(__name__)

            # IA: Resumo automático
            if not self.short_title or not self.preview_summary:
                prompt_title = f"Resuma esse título em até 18 caracteres sem perder o sentido:\nTítulo: {self.title}"
                texto_limpo = strip_tags(self.content)
                prompt_summary = f"Resuma o conteúdo do post abaixo em no máximo 100 caracteres:\n{texto_limpo}"

                from .utils import resumir_texto  # evite import global circular
                resumo_titulo = resumir_texto(prompt_title)
                resumo_conteudo = resumir_texto(prompt_summary)

                logger.warning(f"Resumo título: {resumo_titulo}")
                logger.warning(f"Resumo conteúdo: {resumo_conteudo}")

                self.short_title = resumo_titulo or self.title[:18]
                self.preview_summary = resumo_conteudo or texto_limpo[:100]

            # Geração do slug único
            if not self.slug:
                base_slug = slugify(self.title)
                slug = base_slug
                counter = 1
                while Post.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                self.slug = slug

            super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Image(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    imagem = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f'Imagem de: {self.post.title}'

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comentário de {self.writer.username} em {self.post.title}'

    def is_reply(self):
        return self.parent is not None


class Review(BaseModel):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 a 5 estrelas

    def __str__(self):
        return f'{self.writer.username} avaliou {self.post.title} com {self.rating} estrelas'
    

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)  # Link para onde o usuário será redirecionado
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notificação para {self.recipient.username}: {self.message}'
    

