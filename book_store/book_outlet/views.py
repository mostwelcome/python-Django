from django.shortcuts import render, get_object_or_404

from .models import Book
from django.db.models import Avg


def add_books(request):
    book1 = Book.objects.create(title='book1', rating=4, author='sdutta', is_best_selling=True)
    book2 = Book.objects.create(title='book2', rating=5, author='sdutta', is_best_selling=True)


def index(request):
    books = Book.objects.all().order_by('-rating')
    no_of_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {
        "books": books,
        "no_of_books": no_of_books,
        "avg_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_details.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_best_selling
    })
