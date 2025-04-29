from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




# Cria os modelos da aplicação blog
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        if not self.title:
            raise ValidationError('O título não pode ser vazio.')
        if len(self.text) < 10:
            raise ValidationError('O texto deve ter pelo menos 10 caracteres.')
        
# Imagens dos posts
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)   
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)

# Modelos de comentários
class Comment(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

# Avaliações de posts
class Reviews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.stars)

    # Método para validação personalizada
    def clean(self):
        if self.stars < 1 or self.stars > 5:
            raise ValidationError('A avaliação deve ter entre 1 e 5 estrelas.')


