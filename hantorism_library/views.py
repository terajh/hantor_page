from django.shortcuts import render
from rest_framework import viewsets
from common_hantorism.models import HantorismLibrary as Model


class BookReturnViewSet(viewsets.ModelViewSet):
    def book_return(self, request, book_name, book_owner_name):
        book = Model.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
        book.rent()
        context = {'book': book, 'book_name': book_name}
        return render(request, 'book_return.html', context)

    def book_return_state(self, request, book_name, book_owner_name):
        book = Model.objects.filter(book_name=book_name)

        context = {'book': book, 'book_name': book_name}


class BookRentViewSet(viewsets.ModelViewSet):
    def book_rent(self, request, book_name, book_owner_name):
        book = Model.objects.filter(book_name=book_name)
        context = {'book': book, 'book_name': book_name, 'book_owner_name': book_owner_name}
        return render(request, 'book_rent.html', context)

    def book_rent_state(self, request, book_name, book_owner_name):
        book = Model.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
        book.rent()


def library(request):
    books = Model.objects.all()
    context = {'books': books}
    return render(request, 'library.html', context)


