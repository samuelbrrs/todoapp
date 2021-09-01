from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.user_login, name='user_login'),
    path('sair/', views.user_logout, name='user_logout'),
    path('alterar-senha/', views.user_change_password, name='user_change_password'),
    path('meu-perfil/', views.list_user_profile, name='list_user_profile'),
    path('novo-perfil/', views.add_user_profile, name='add_user_profile'),
    path('alterar-perfil/<username>/', views.change_user_profile, name='change_user_profile'),
    path('alterar-usuário/<username>/', views.change_user_information, name='change_user_information'),
]