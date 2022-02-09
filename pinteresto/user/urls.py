from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

app_name = 'user'
urlpatterns = [
    path('post/', post, name='post'),
    path('author/<int:user_id>', author, name='author'),
    path('register/', register, name='register'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('delety/<int:pk>', delety, name='delety')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

