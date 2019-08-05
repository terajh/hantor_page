from django.urls import path
from .views import ViewSet,userList,userDetail

as_view = ViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('sign_up/', as_view),
    path('user_list/',userList,name='user_list'),
    path('user_list/detail-<str:ID>/',userDetail,name='user_detail'),
]
