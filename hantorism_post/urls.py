from django.urls import path,re_path
from . import views

as_view = views.ViewSet.as_view({
    'get': 'post_list',
    'post': 'create'
})

urlpatterns = [
    path('posts/', as_view, name='post_list'),
    path('post_write/', views.postWrite,name='post_write'),
    path('do_post/',views.doPost,name='do_post'),
    path('post_view/',views.postView,name='post_view'),
    path('post_modify/',views.postModify,name='post_modify'),
    path('update_post/',views.updatePost,name='update_post'),
    path('post_delete/',views.postDelete,name='post_delete'),
    path('create_comment/', views.create_comment, name='create_comment')
]
