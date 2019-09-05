from django.urls import path
from . import views

urlpatterns = [
    path(r'desk/', views.desk, name='desk')
]