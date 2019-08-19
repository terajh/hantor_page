from django.urls import path,re_path
from .views import ViewSet,postWrite,doPost,postView,postSearch,postModify,updatePost,postDelete,titleSearch

as_view = ViewSet.as_view({
    'get': 'postList',
    'post': 'create'
})

urlpatterns = [
    path('posts/', as_view, name='post_list'),
    path('post_write/', postWrite,name='post_write'),
    path('do_post/',doPost,name='do_post'),
    path('post_view/',postView,name='post_view'),
    path('post_search/',postSearch,name='post_search'),
    path('post_modify/',postModify,name='post_modify'),
    path('update_post/',updatePost,name='update_post'),
    path('post_delete/',postDelete,name='post_delete'),
    path('title_search/',titleSearch,name='title_search')
]
