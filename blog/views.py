from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly , AllowAny
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment, Reviews, Image
from .serializers import BlogSerializer, CommentSerializer, ReviewSerializer, ImageSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Apenas leitores podem ver, mas só o superusuário pode editar/criar

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("Somente o superusuário pode criar posts.")
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Qualquer usuário autenticado pode criar avaliações
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            raise PermissionDenied("Somente o superusuário pode adicionar imagens.")
        serializer.save(user=self.request.user)
