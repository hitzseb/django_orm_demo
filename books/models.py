from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, blank=True, null=True)
    birth = models.CharField(max_length=100, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100, blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    
    def __str__(self):
        return f'{self.title} | by {self.author.name}'