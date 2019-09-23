from django.urls import path,re_path
from . import views

as_view = views.ViewSet.as_view({
    'get': 'overflow_list',
    'post': 'create'
})

urlpatterns = [
    path('overflows/', as_view, name='overflow_list'),
    path('overflow_write/', views.overflow_write,name='overflow_wrte'),
    path('do_overflow/',views.do_overflow,name='do_overflow'),
    path('overflow_view/',views.overflow_view,name='overflow_view'),
    path('overflow_modify/',views.overflow_modify,name='overflow_modify'),
    path('update_overflow/',views.update_overflow,name='update_overflow'),
    path('overflow_delete/',views.overflow_delete,name='overflow_delete'),
    path('create_answer/', views.create_answer, name='create_answer'),
    path('overflow_select/',views.overflow_select,name='overflow_select')
]
