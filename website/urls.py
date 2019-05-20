from django.urls import path
from . import views, views_user

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views_user.login_view, name='login'),
    path('logout', views_user.logout_view, name='logout'),
    path('register', views_user.registration, name='registration'),
]