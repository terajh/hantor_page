from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets

from common_hantorism.models import HantorismUser


class SignUpViewSet(viewsets.ModelViewSet):
    def go_to_sign_up(self, request):
        return render(request, 'sign_up.html')

    def sign_up(self, request):
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
    def go_to_sign_in(self, request):
        return render(request, 'sign_in.html')

    def sign_in(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            message = ''
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('list')

            message = 'fail'
            return render(request, "list.html", {'message': message})


def user_page(request):
    user = HantorismUser.objects.get(user__username=request.GET['userID'])
    user_info = HantorismUser.objects.get(user_id=user.id)
    return render(request, "user_page.html", {'user_info': user_info,
                                              'userID': request.GET['userID']})


@login_required
def sign_out(request):
    auth.logout(request)
    return redirect('list')


@login_required
def my_page(request):
    user_detail = HantorismUser.objects.get(user_id=request.user.id)
    context = {'user_detail': user_detail,
               'change': 2}
    return render(request, 'my_page.html', context)


@login_required
def change_password(request):
    user = request.user
    password_form = PasswordChangeForm(user, request.POST)
    user_detail = HantorismUser.objects.get(user_id=request.user.id)
    context = {'user_detail': user_detail,
               'change': 2}
    if password_form.is_valid():
        password_form.save()
        update_session_auth_hash(request, password_form.user)
        context['change'] = 1
        return render(request, 'my_page.html', context)
    else:
        context['change'] = 0
        return render(request, 'my_page.html', context)
