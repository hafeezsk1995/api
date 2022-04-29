from django.urls import path
from . views import GetMovieById, GetMovieByTitle, GetMovieByYear, GetMoviesByGenres, GetMoviesByGivenHigherRating

urlpatterns = [
   path('', GetMovieByTitle.as_view(), name='Endpoint for getting records by title'), 
   path('get_by_id/<int:pk>', GetMovieById.as_view(), name='Endpoint for getting records by id'),   
   path('get_by_year', GetMovieByYear.as_view(), name='Endpoint for getting records by year'),   
   path('get_by_higher_ratings', GetMoviesByGivenHigherRating.as_view(), name='Endpoint for getting records by year'),   
   path('get_by_genres', GetMoviesByGenres.as_view(), name='Endpoint for getting records by genres'),   
   
   
]