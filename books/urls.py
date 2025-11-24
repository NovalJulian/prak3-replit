from django.urls import path

from . import views

urlpatterns = [
    # /books/
    path('', views.index, name='books.index'),
]
