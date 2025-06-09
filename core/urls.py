from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from blog.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('logout/', logout_view, name='logout'),

]
