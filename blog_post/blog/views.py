# Create your views here.
from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    pass


def post_details(request):
    pass
