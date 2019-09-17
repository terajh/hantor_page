from django.urls import path
from . import views

urlpatterns = [
    path(r'desk/', views.dodesk, name='dodesk'),
    path(r'desk_list/',views.desk_list, name='desk_list')
]