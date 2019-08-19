from django.urls import path
from . import views


urlpatterns = [
    path('library/', views.library, name='library'),
    path(r'book_return/<book_name>/<book_owner_name>/', views.book_return),
    path(r'book_rent/<book_name>/<book_owner_name>/', views.book_rent),
]