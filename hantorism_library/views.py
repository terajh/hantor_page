from django.shortcuts import render
from .models import Library


def library(request):
    books = Library.objects.all()
    context = {'books': books}
    return render(request, 'library.html', context)
