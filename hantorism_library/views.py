from django.shortcuts import render
from common_hantorism.models import HantorismBook, HantorismRentBook


def book_return(request, book_name, book_owner_name):
    book = HantorismRentBook.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
    return_books = HantorismRentBook.objects.filter(book_name=book_name).get(book_owner_name=book_owner_name)
    if request.method == "POST":
        # book.book_rent_state = False
        for book in book:
            book.book_return()
        for return_book in return_books:
            return_book.delete()
        books = HantorismBook.objects.all()
        context = {'books': books}
        return render(request, 'library.html', context)

    context = {'book': book, 'book_name': book_name, 'book_owner_name': book_owner_name, 'return_boooks': return_books}
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
