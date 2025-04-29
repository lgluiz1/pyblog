from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment, Reviews, Image
from .serializers import BlogSerializer, CommentSerializer, ReviewSerializer, ImageSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Apenas leitores podem ver, mas só o superusuário pode editar/criar

    def perform_create(self, serializer):
        # Garantir que o 'user' seja atribuído automaticamente ao criar um novo post
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("Somente o superusuário pode criar comentários.")
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("Somente o superusuário pode criar avaliações.")
        serializer.save(user=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("Somente o superusuário pode adicionar imagens.")
        serializer.save(user=self.request.user)
