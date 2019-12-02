from django.urls import include, path
from . import views

app_name = 'list_book'
urlpatterns = [
    path('', views.index, name = 'index'),
]