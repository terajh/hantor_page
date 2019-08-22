from common_hantorism.models import HantorismUser
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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
            isHantor=request.data['is_hantor'])
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
