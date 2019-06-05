from django.urls import path
from . import views, views_user, views_loggedin, views_forms

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views_user.login_view, name='login'),
    path('logout', views_user.logout_view, name='logout'),
    path('register', views_user.registration, name='registration'),
    #user logged in urls
    path('home', views_loggedin.home, name='home'),
    path('aboutlog', views_loggedin.about, name='aboutlog'),

    path('newplan', views_loggedin.newplan, name='newplan'),
    path('showplan', views_forms.showplan, name='showplan'),
    path('saveplan', views_forms.saveplan, name='saveplan'),

    path('settings', views_loggedin.settings, name='settings'),
    path('settinginfo', views_forms.settinginfo, name='settinginfo'),
    path('settingpwd', views_forms.settingpwd, name='settingpwd'),

    path('help', views_loggedin.help, name='help'),
    path('manageplans', views_loggedin.manageplans, name='manageplans'),
    path('group', views_loggedin.group, name='group'),
    path('managegroups', views_loggedin.managegroups, name='managegroups'),
]