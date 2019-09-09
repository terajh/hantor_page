from django.urls import path,re_path
from . import views

as_view = views.ViewSet.as_view({
    'get': 'overflow_list',
    'post': 'create'
})

urlpatterns = [
    path('overflows/', as_view, name='overflow_list'),
    path('overflow_write/', views.overflowWrite,name='overflow_wrte'),
    path('do_overflow/',views.doOverflow,name='do_overflow'),
    path('overflow_view/',views.overflowView,name='overflow_view'),
    path('overflow_search/',views.overflowSearch,name='overflow_search'),
    path('overflow_modify/',views.overflowModify,name='overflow_modify'),
    path('update_overflow/',views.updateOverflow,name='update_overflow'),
    path('overflow_delete/',views.overflowDelete,name='overflow_delete'),
    path('create_answer/', views.create_answer, name='create_answer'),
    path('overflow_select/',views.overflowSelect,name='overflow_select')
]
