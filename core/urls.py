from django.urls import path
from .views import Home, ProfileList, ProfileCreate, MovieList, MovieDetails, MovieShow

app_name = 'core'

urlpatterns = [
    path('', Home.as_view()),
    path('profile', ProfileList.as_view(), name='profile_list'),
    path('profile/create', ProfileCreate.as_view(), name='profile_create'),
    path('movies/<str:profile_id>', MovieList.as_view(), name='movie_list'),
    path('movie/details/<str:movie_id>', MovieDetails.as_view(), name='movie_details'),
    path('movie/play/<str:movie_id>', MovieShow.as_view(), name='movie_show'),
]
