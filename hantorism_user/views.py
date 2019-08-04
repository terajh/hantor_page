from common_hantorism.models import HantorismUser
from rest_framework import viewsets
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone


class SignUpViewSet(viewsets.ModelViewSet):
    def gotoSignUp(self, request):
        return render(request, 'sign_up.html')
    def signUp(self, request):
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                        username=request.POST['ID'],
                        password=request.POST['password1'])
            hantorism_user = HantorismUser(
                        user=user,
                        name=request.POST['name'],
                        studentNum=request.POST['studentNum'],
                        major=request.POST['major'],
#                        gender=request.POST['gender'],
                        email=request.POST['email'])
#                        isHantor=request.data['isHantor'])
            hantorism_user.save()
            auth.login(request,user)
        return redirect('list')

class SignInViewSet(viewsets.ModelViewSet):
    def gotoSignIn(self,request):
        return render(request,'sign_in.html')
    def signIn(self,request):
        if request.method == "POST":
            userID = request.POST['ID']
            userPW = request.POST['password']
            user = auth.authenticate(request,username=userID, password=userPW)
            if user is not None :
                auth.login(request,user)
                return render(request,'WelcomLogin.html',{})
            return render(request,'FailLogin.html',{})

@login_required
def userList(request):
    user_list=HantorismUser.objects.order_by()
    context={'user_list':user_list}
    return render(request,'user_list.html',context)

@login_required
def userDetail(request, name):
    user_detail=HantorismUser.objects.get(name=name)
    context={'user_detail':user_detail}
    return render(request,'user_detail.html',context)

@login_required
def signOut(request):
    auth.logout(request)
    return redirect('list')