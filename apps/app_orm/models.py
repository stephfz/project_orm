#modelmanager
from __future__ import unicode_literals
from django.db import models
import re

class Genre(models.Model):
    genre = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=45)
    nationality = models.CharField(max_length=45)
    #genre = models.ManyToManyField(Genre, related_name='director_genres')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MovieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 5:
            errors["title"] = "El titulo debe contener por lo menos 5 caracteres"
        if len(postData['description']) < 10:
            errors["description"] = "La descripcion contener por lo menos 10 caracteres"
        if len(postData['duration_in_mins']) <= 0 or int(postData['duration_in_mins']) > 0:
            errors["duration_in_mins"] = "La duracion debe ser mayor a cero"    
        return errors        

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration_in_mins = models.IntegerField()
    director = models.ForeignKey(Director, related_name = 'movies', on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, related_name = 'movies', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = MovieManager()  

    def __str__(self):
        return f"{self.id} , {self.title}"


class UserManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['name']) < 2:
            errors["name"] = "El nombre debe tener mas de 2 caracteres"
        errorEmail = self.checkEmail(postData["email"])
        if len(errorEmail) >0 :
            errors["email"] = errorEmail
        return errors      

    def checkEmail(self, data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data):          
            errors['email'] = "Correo Invalido"
        return errors      


class User(models.Model):
    name = models.CharField(max_length=45, blank = False, null =False)
    lastname = models.CharField(max_length=45, blank = True, null =True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()          


