from django.urls import path
from books import views

urlpatterns = [
    path('', views.books_base, name='home'),
    
    # Author URLs
    path('autores/', views.author_list, name='author_list'),
    path('autores/<int:pk>/', views.author_detail, name='author_detail'),
    path('autores/crear/', views.author_create, name='author_create'),
    path('autores/editar/<int:pk>/', views.author_edit, name='author_edit'),
    path('autores/eliminar/<int:pk>/', views.author_delete, name='author_delete'),

    # Genre URLs
    path('generos/', views.genre_list, name='genre_list'),
    path('generos/<int:pk>/', views.genre_detail, name='genre_detail'),
    path('generos/crear/', views.genre_create, name='genre_create'),
    path('generos/editar/<int:pk>/', views.genre_edit, name='genre_edit'),
    path('generos/eliminar/<int:pk>/', views.genre_delete, name='genre_delete'),

    # Book URLs
    path('libros/', views.book_list, name='book_list'),
    path('libros/<str:genre>', views.books_by_genre, name='books_by_genre'),
    path('libros/<int:pk>/', views.book_detail, name='book_detail'),
    path('libros/crear/', views.book_create, name='book_create'),
    path('libros/editar/<int:pk>/', views.book_edit, name='book_edit'),
    path('libros/eliminar/<int:pk>/', views.book_delete, name='book_delete'),
]
