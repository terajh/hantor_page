from django.urls import path
from .views import SignUpViewSet,SignInViewSet,userList,userDetail,signOut

as_signupview = SignUpViewSet.as_view({
    'get': 'gotoSignUp',
    'post': 'signUp'
})

as_signinview = SignInViewSet.as_view({
    'get' : 'gotoSignIn',
    'post' : 'signIn'
})

urlpatterns = [
    path('sign_up/', as_signupview, name='sign_up'),
    path('sign_in/', as_signinview, name='sign_in'),
    path('user_list/', userList, name='user_list'),
    path('user_list/detail-<str:name>/', userDetail, name='user_detail'),
    path('sign_out/',signOut,name='sign_out'),
]
