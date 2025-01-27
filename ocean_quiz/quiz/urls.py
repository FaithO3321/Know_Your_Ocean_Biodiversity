from django.urls import path
from .views import get_quiz, index

urlpatterns = [
    # Home page route
    path('', index, name='index'),

    #API endpoint to fetch the quiz questions
    path('api/get-quiz/', get_quiz, name='get_quiz'),
]
