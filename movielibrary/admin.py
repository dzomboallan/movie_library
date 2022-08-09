from django.contrib import admin
from .models import Actor, Genre, Movie, MovieInstance

# Register your models here.
class MovieInstanceInline(admin.TabularInline):
    model = MovieInstance

class MovieInline(admin.TabularInline):
    model = Movie

#admin.site.register(Movie)
# Register the Admin class for Movie using the decorator
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'actor', 'display_genre')
    inlines  = [MovieInstanceInline]

#admin.site.register(Actor)
# Deffine the admin class
class ActorAdmin(admin.ModelAdmin):
    # Register the admin class with the associated model
    list_display = ('last_name','first_name')
    fields = ['first_name', 'last_name']
    inlines = [MovieInline]

admin.site.register(Actor, ActorAdmin)

admin.site.register(Genre)

#admin.site.register(MovieInstance)
@admin.register(MovieInstance)
class MovieInstanceAdmin(admin.ModelAdmin):
    list_display = ('movie','status','id')
    list_filter = ('status','imprint')
    fieldsets = (
        (None, {'fields':('movie','imprint')}),
        ('Availability',{'fields':('status','id')}),
    )
