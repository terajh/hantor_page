from django.shortcuts import render, redirect
from common_hantorism.models import HantorismBook, HantorismRentBook, HantorismUser
from django.utils import timezone


def book_return(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    return_books = HantorismRentBook.objects.get(book_id=book_id)
    if request.method == "POST":
        book.book_return()
        return_books.delete()
        books = HantorismBook.objects.all()
        context = {'books': books}
        return redirect('/../../library/')
    elif request.method == "GET":
        context = {'book': book, 'return_books': return_books}
        return render(request, 'book_return.html', context)


def book_rent(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    current_user = HantorismUser.objects.get(user=request.user)
    time = timezone.now()
    if request.method == "POST":
        book.state = True;
        book.save()
        book = HantorismRentBook(date=time, user=current_user, book=book)
        book.save()
        return redirect('/../../library/')


def library(request):
    books = HantorismBook.objects.all()
    return_books = HantorismRentBook.objects.all()
    context = {'books': books, 'return_books': return_books}
    return render(request, 'library.html', context)
