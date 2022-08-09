from turtle import title
from django.shortcuts import render
from django.views import generic
from .models import Movie, Actor, MovieInstance, Genre

# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()

    # Available movies 
    num_instances_available = MovieInstance.objects.filter(status__exact = 'a').count()

    # The 'all()' is implied by default.
    num_actors = Actor.objects.count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    # Genre
    num_genre = Genre.objects.count()

    # Movies tha contain a particular word
    num_title = Movie.objects.filter(title__exact = 'Two').count()

    context = {
        'num_movies': num_movies,
        'num_instances': num_instances,
        'num_instances_available' : num_instances_available,
        'num_actors' : num_actors,
        'num_genre' : num_genre,
        'num_title' : num_title,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 10

class MovieDetailView(generic.DetailView):
    model = Movie

class ActorListView(generic.ListView):
    model = Actor

class ActorDetailView(generic.DetailView):
    model = Actor