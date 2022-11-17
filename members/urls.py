from django.urls import path
from . import views

urlpatterns = [
    path('user_login', views.login_user, name='user-login'),
    path('logout_user', views.logout_user, name='user-logout'),
    path('signup/', views.signup, name='user-register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
