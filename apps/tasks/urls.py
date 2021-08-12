from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('adicionar/', views.add_category, name='add_category'),
]