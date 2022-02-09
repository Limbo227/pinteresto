from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *


app_name = 'news'
urlpatterns = [
    path('', index, name='home'),
    path('post/<int:pk>', news, name='detail'),
    path('create_post/', addpost_new, name='add_post'),
    path('post_edit', post_edit, name='post_edit'),
    path('delete_com/<int:pk>', delete_com, name='delete_com'),
    path('search/', search, name='search')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

