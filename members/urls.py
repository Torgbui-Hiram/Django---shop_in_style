from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='user-register'),
    path('user_login', views.login_user, name='user-login'),
    path('logout_user', views.logout_user, name='user-logout'),
]
