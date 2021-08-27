from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_books),
    path('<int:id>', views.book_details, name='book_detail')
]
