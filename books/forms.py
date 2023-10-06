from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'origin', 'birth', 'picture', 'bio']
        
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'date', 'cover', 'synopsis', 'author', 'genres']