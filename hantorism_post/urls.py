from django.urls import path,re_path
from . import views

as_view = views.ViewSet.as_view({
    'get': 'post_list',
    'post': 'create'
})

urlpatterns = [
    path('posts/', as_view, name='post_list'),
    path('post_write/', views.post_write,name='post_write'),
    path('do_post/',views.do_post,name='do_post'),
    path('post_view/',views.post_view,name='post_view'),
    path('post_modify/',views.post_modify,name='post_modify'),
    path('update_post/',views.update_post,name='update_post'),
    path('post_delete/',views.post_delete,name='post_delete'),
    path('create_comment/', views.create_comment, name='create_comment')
]
