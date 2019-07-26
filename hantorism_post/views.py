from common_hantorism.models import HantorismPost as Model
from rest_framework import viewsets
from django.shortcuts import render
from django.utils import timezone


class ViewSet(viewsets.ModelViewSet):
    def list(self, request):
        posts = Model.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return render(request, 'post_list.html', {'posts': posts})

    def create(self, request):
        posts = Model.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return render(request, 'post_list.html', {'posts': posts})