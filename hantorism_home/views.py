from django.shortcuts import render


def list(request):
    return render(request, 'list.html', {})

def contact(request):
    return render(request, 'contact.html')