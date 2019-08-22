from django.urls import path
from . import views


urlpatterns = [
    path('library/', views.library, name='library'),
    path('book_return/<book_id>/', views.book_return),
    path('book_rent/<book_name>/<book_owner_name>/', views.book_rent),
]