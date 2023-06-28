from django.urls import path
from .views import register_user
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]




