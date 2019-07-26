from django.urls import path
from .views import ViewSet

as_view = ViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('post/', as_view, name='post_list'),
]
