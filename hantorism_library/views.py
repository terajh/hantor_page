from django.shortcuts import render
from common_hantorism.models import HantorismLibrary as Model


def book_return(request, book_name, book_owner_name):
    book = Model.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
    if request.method == "PUT":
        book.book_rent_state = False
        book.book_return()
        books = Model.objects.all()
        context = {'books': books}
        return render(request, 'library.html', context)
    context = {'book': book, 'book_name': book_name, 'book_owner_name': book_owner_name}
    return render(request, 'book_return.html', context)


def book_rent(request, book_name, book_owner_name):
    book = Model.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
    context = {'book': book, 'book_name': book_name, 'book_owner_name': book_owner_name}
    return render(request, 'book_rent.html', context)


def library(request):
    books = Model.objects.all()
    context = {'books': books}
    return render(request, 'library.html', context)


