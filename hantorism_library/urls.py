from django.urls import path
from . import views
from .views import BookRentViewSet, BookReturnViewSet

as_bookrentview = BookRentViewSet.as_view({
    'get': 'book_rent_state',
    'put': 'book_rent'
})

as_bookreturnview = BookReturnViewSet.as_view({
    'get': 'book_return_state',
    'put': 'book_return'
})

urlpatterns = [
    path('library/', views.library, name='library'),
    path(r'book_return/<book_name>/<book_owner_name>/', as_bookreturnview),
    path(r'book_rent/<book_name>/<book_owner_name>/', as_bookrentview),
]