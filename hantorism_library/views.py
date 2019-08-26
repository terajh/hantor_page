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
        return_books.return_request = True
        return_books.save()
        return redirect('/../../library/')


@login_required()
def return_admin(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    return_books = HantorismRentBook.objects.get(book_id=book_id)
    if request.method == "POST":
        return_books.delete()
        book.state = "Able"
        book.save()
        return redirect('/../../library_admin/')


@login_required()
def book_rent(request, book_id):
    book = HantorismBook.objects.get(id=book_id)
    current_user = HantorismUser.objects.get(user=request.user)
    time = timezone.now()
    if request.method == "POST":
        rent_book = HantorismRentBook(date=time, user_info=current_user, book=book, return_request=False)
        rent_book.rent()
        rent_book.save()
        return redirect('/../../library/')


def rent_admin(request, book_id):
    if request.method == "POST":
        rent_book = HantorismRentBook.objects.get(book_id=book_id)
        rent_book.rent_admin()
        rent_book.save()
        return redirect('/../../library_admin/')


@login_required()
def library(request):
    books = HantorismBook.objects.all()
    return_books = HantorismRentBook.objects.all()
    context = {'books': books, 'return_books': return_books}
    return render(request, 'library.html', context)


@login_required()
def library_admin(request):
    rent_books = HantorismRentBook.objects.all()
    books = HantorismBook.objects.all()
    current_user = HantorismUser.objects.get(user=request.user)
    permission = current_user.is_admin
    context = {'books': books, 'rent_books': rent_books, 'permission': permission}
    return render(request, 'library_admin.html', context)
