from django.urls import path
from . import views, views_user, views_loggedin

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views_user.login_view, name='login'),
    path('logout', views_user.logout_view, name='logout'),
    path('register', views_user.registration, name='registration'),
    #user logged in urls
    path('home', views_loggedin.home, name='home'),
    path('aboutlog', views_loggedin.about, name='aboutlog'),

]