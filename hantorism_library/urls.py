from django.urls import path

from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path('book_return/<book_id>/', views.book_return),
    path('book_rent/<book_id>/', views.book_rent),
    path('library_admin/', views.library_admin),
    path('return_admin/<book_id>/', views.return_admin),
    path('rent_admin/<book_id>/', views.rent_admin),
]