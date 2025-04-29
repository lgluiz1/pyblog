from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, ReviewViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'posts', BlogViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
