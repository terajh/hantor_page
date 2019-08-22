from django.shortcuts import render, redirect
from common_hantorism.models import HantorismBook, HantorismRentBook


def book_return(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    return_books = HantorismRentBook.objects.get(rent_book_id=book_id)
    if request.method == "POST":
        book.book_return()
        return_books.delete()
        books = HantorismBook.objects.all()
        context = {'books': books}
        return redirect('/../../library/')
    elif request.method == "GET":
        context = {'book': book, 'return_books': return_books}
        return render(request, 'book_return.html', context)


def book_rent(request, book_name, book_owner_name):
    book = HantorismBook.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
    context = {'book': book, 'book_name': book_name, 'book_owner_name': book_owner_name}
    return render(request, 'book_rent.html', context)


def library(request):
    books = HantorismBook.objects.all()
    return_books = HantorismRentBook.objects.all()
    context = {'books': books, 'return_books': return_books}
    return render(request, 'library.html', context)
