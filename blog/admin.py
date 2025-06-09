from django.contrib import admin
from .models import Post, Category, Comment, Image, Review, Tags, Notification

class PostAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.groups.filter(name='autores').exists()

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(Tags)
admin.site.register(Notification)

