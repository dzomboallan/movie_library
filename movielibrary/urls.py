from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
    path('actor/', views.ActorListView.as_view(), name='actor'),
    path('actor/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),
    # path('movie/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
