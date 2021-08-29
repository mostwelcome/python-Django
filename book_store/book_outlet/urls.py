from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_books),
    path('<slug:slug>', views.book_detail, name='book_detail')
]
