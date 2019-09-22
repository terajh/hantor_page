from django.urls import path
from .views import SignUpViewSet, SignInViewSet, user_page, sign_out, my_page, change_password

as_signupview = SignUpViewSet.as_view({
    'get': 'go_to_sign_up',
    'post': 'sign_up'
})

as_signinview = SignInViewSet.as_view({
    'get': 'go_to_sign_in',
    'post': 'sign_in'
})

urlpatterns = [
    path('sign_up/', as_signupview, name='sign_up'),
    path('sign_in/', as_signinview, name='sign_in'),
    path('user_page/', user_page, name='user_page'),
    path('sign_out/', sign_out, name='sign_out'),
    path('my_page/', my_page, name='my_page'),
    path('change_pw', change_password, name='change_pw')
]
