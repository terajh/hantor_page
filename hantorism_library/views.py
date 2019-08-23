from django.shortcuts import render, redirect
from common_hantorism.models import HantorismBook, HantorismRentBook, HantorismUser
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required()
def book_return(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    return_books = HantorismRentBook.objects.get(book_id=book_id)
    if request.method == "POST":
        book.book_return()
        return_books.delete()
        return redirect('/../../library/')


@login_required()
def book_rent(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    current_user = HantorismUser.objects.get(user=request.user)
    time = timezone.now()
    if request.method == "POST":
        book.state = "Wait"
        book.save()
        rent_book = HantorismRentBook(date=time, user_info=current_user, book=book)
        rent_book.save()
        return redirect('/../../library/')


@login_required()
def library(request):
    books = HantorismBook.objects.all()
    return_books = HantorismRentBook.objects.all()
    context = {'books': books, 'return_books': return_books}
    return render(request, 'library.html', context)
