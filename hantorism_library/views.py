from django.shortcuts import render
from common_hantorism.models import HantorismLibrary as Model


def library(request):
    books = Model.objects.all()
    context = {'books': books}
    return render(request, 'library.html', context)
