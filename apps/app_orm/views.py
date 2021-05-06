from django.shortcuts import render, redirect
from .models import Movie, Director, Genre, User
from django.contrib import messages
from django.http import JsonResponse

import bcrypt

# Create your views here.

def index(request):
    #if request.session['logged_user']:
     #   print('user: ', request.session['logged_user'])

    return render(request, 'index.html')

def all_movies(request):
    movies = Movie.objects.all()
    context = {
                'movies' : movies
            }
    return render(request, 'movie_catalog.html', context) 


def movie(request):  
    if request.method == 'GET':
        directors = Director.objects.all()
        genres = Genre.objects.all()
        context = {'directors' : directors, 'genres':genres }
        return render(request, 'movie.html', context)
    else:
        director = Director.objects.get( id = int(request.POST['director']) )
        genre = Director.objects.get( id = int(request.POST['genre']) )
        # validar datos
        errors = Movie.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, key)
            return redirect('/movie')    
        else:
            Movie.objects.create(
                        title = request.POST['title'],
                        description = request.POST['description'],
                        release_date  =request.POST['release_date'],
                        duration_in_mins = request.POST['duration_in_mins'],
                        director = director,
                        genre = genre
                )
            return redirect('/movies')

    
def director(request):
    if request.method == 'GET':
        directors =  Director.objects.all()
        context = {'directors' : directors}
        return render(request, 'director.html', context)
    else:

        Director.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            nationality = request.POST['nationality']
        )
        return redirect('/director')   

def genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        context = {'genres' : genres}
        return render(request, 'genres.html', context)
    else:
        Genre.objects.create(genre = request.POST['genre'])
        return redirect('/genres')

def director_movies(request, director_id):
    director = Director.objects.get(id = int(director_id))
    context = {'director' : director}
    return render(request, 'movies.html', context)

def genre_movies(request, genre_id):
    genre = Genre.objects.get(id =int(genre_id)) 
    context = {'genre' : genre}
    return render(request, 'genre_movies.html', context)   


def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print (pw_hash)
        user = User.objects.create(
            name = request.POST['name'], 
            password = pw_hash,
            lastname = request.POST['lastname'],
            email = request.POST['email']
        )
        request.session['logged_user'] = user.name
        return redirect("/") 

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        results = User.objects.filter(email=request.POST['email'])
        print('user: ' , results)
        if results:
            logged_user = results[0]
            print('logged_user: ', logged_user)
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user'] = logged_user.name   
                return redirect("/")
    return redirect('/login')

def logout(request):
    try:
        del request.session['logged_user']
    except:
        print('Error')
    return redirect("/")    


def checkEmail(request):
    print("****** Validando Email ******")
    error = User.objects.checkEmail(request.POST["email"])
    print ('error: ', error)
    #return redirect('/register')
    return JsonResponse({'errors': error})      
