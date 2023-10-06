from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .forms import *

def is_admin(user):
    return user.is_authenticated and user.is_staff

def books_base(request):
    return render(request, 'books_base.html')

# Author CRUD

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})

@user_passes_test(is_admin)
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'author_create.html', {'form': form})
    
@user_passes_test(is_admin)
def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid:
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_edit.html', {'form': form, 'author':author})
    
@user_passes_test(is_admin)
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('author_list')

# Genre CRUD

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'genre_detail.html', {'genre': genre})

@user_passes_test(is_admin)
def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'genre_create.html', {'form': form})
    
@user_passes_test(is_admin)
def genre_edit(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_edit.html', {'form': form, 'genre':genre})
    
@user_passes_test(is_admin)
def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genre.delete()
    return redirect('genre_list')

# Book CRUD

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def books_by_genre(request, genre):
    books = Book.objects.filter(genres__name=genre)
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    genres = book.genres.all()
    return render(request, 'book_detail.html', {'book': book, 'genres':genres})


@user_passes_test(is_admin)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})
    
@user_passes_test(is_admin)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_edit.html', {'form': form, 'book':book})
    
@user_passes_test(is_admin)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
