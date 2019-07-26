from common_hantorism.models import HantorismUser as Model
from rest_framework import viewsets
from django.shortcuts import render
from django.utils import timezone


class ViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return render(request, 'sign_up.html')

    def create(self, request):
        print(request.data)
        return render(request, 'sign_up.html')
