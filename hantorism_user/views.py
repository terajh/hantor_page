from common_hantorism.models import HantorismUser
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class SignUpViewSet(viewsets.ModelViewSet):
    def gotoSignUp(self, request):
        return render(request, 'sign_up.html')

    def signUp(self, request):
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'])

        hantorism_user = HantorismUser(
            user=user,
            name=request.POST['name'],
            student_number=request.POST['student_number'],
            major=request.POST['major'],
            gender=request.POST['gender'],
            email=request.POST['email'],
            is_hantor=request.data['is_hantor'])
        try:
            hantorism_user.save()
            auth.login(request, user)
            return redirect('list')
        except Exception as ex:
            print(ex)


class SignInViewSet(viewsets.ModelViewSet):
    def gotoSignIn(self, request):
        return render(request, 'sign_in.html')

    def signIn(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'WelcomLogin.html', {})
            return render(request, 'FailLogin.html', {})


@login_required
def userList(request):
    user_list = HantorismUser.objects.order_by()
    context = {'user_list': user_list}
    return render(request, 'user_list.html', context)


@login_required
def userDetail(request, name):
    user_detail = HantorismUser.objects.get(name=name)
    context = {'user_detail': user_detail}
    return render(request, 'user_detail.html', context)


@login_required
def signOut(request):
    auth.logout(request)
    return redirect('list')


@login_required
def myPage(request):
    user_detail = HantorismUser.objects.get(user_id=request.user.id)
    context = {'user_detail': user_detail,
               'change':2}
    return render(request, 'my_page.html', context)

@login_required
def changePW(request):
    user=request.user
    password_form=PasswordChangeForm(user,request.POST)
    user_detail = HantorismUser.objects.get(user_id=request.user.id)
    context = {'user_detail': user_detail,
               'change':2}
    if password_form.is_valid():
        password_form.save()
        update_session_auth_hash(request,password_form.user)
        context['change']=1
        return render(request,'my_page.html',context)
    else:
        context['change']=0
        return render(request,'my_page.html',context)