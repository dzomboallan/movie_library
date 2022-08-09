import uuid # Required for unique movie instances
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class Genre(models.Model):
    """Model representing a movie genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre(e.g. Sci-fi)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Movie(models.Model):
    """Model representing a movie"""
    title = models.CharField(max_length=200)
    # Foreign key used because a movie can only have one writer but a writer  can have multiple movies
    # Writer as a string rather than an object  because it hasn't been declared yet in the file.

    actor = models.ForeignKey('Actor', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the movuie')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many movies. Movies can cover many genres
    # Genre class has already been defined so wwe can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the model object."""
        return self.title

    def get_absolute_url(self):
        """Return the url to access a detail record for this book."""
        return reverse('movie-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

class MovieInstance(models.Model):
    """Model representing a specific copy of a movie"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    help_text='Unique ID for this particular movie across the whole library.')
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)

    AVAILABILITY_STATUS =(
        ('a','Available'),
        ('n','Not available'),
        ('r','Reserved')
    )
    
    status = models.CharField(max_length=1, choices=AVAILABILITY_STATUS,
    blank = True, default = 'a', help_text='Movie availability')

    class Meta:
        ordering = ['status']
        # permissions = (("can_mark_available","Set movie as available"))

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}({self.movie.title})'

class Actor(models.Model):
    """Model representing an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        """Returns the uRL to access a particular writer instance"""
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the model object."""
        return f'{self.last_name},{self.first_name}'

class Language(models.Model):
    """Model representing language"""
    lang = models.CharField(max_length=100, help_text='Enter the language for the movie(e.g. English)')

    def __str__(self):
        """String representing the Model object"""
        return self.lang
