from common_hantorism.models import HantorismUser as Model
from rest_framework import viewsets
from django.shortcuts import render,redirect
from .forms import signUpForm
from django.utils import timezone


class ViewSet(viewsets.ModelViewSet):
    def list(self, request):
        form=signUpForm(request.GET)
        return render(request, 'sign_up.html',{'form':form})

    def create(self, request):
        form=signUpForm(request.POST)
        if form.is_valid():
            obj = Model(ID=form.data['ID'],
                        PW=form.data['PW'],
                        name=form.data['name'],
                        studentNum=form.data['studentNum'],
                        major=form.data['major'],
                        gender=form.data['gender'],
                        email=form.data['email'],
                        isHantor=form.data['isHantor'])
            obj.save()
        return redirect('user_list')

def userList(request):
    user_list=Model.object.order_by('name')
    context={'user_list':user_list}
    return render(request,'user_list.html',context)

def userDetail(request, ID):
    user_detail=Model.object.get(pk=ID)
    context={'user_detail':user_detail}
    return render(request,'user_detail.html',context)