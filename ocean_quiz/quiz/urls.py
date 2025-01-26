from django.urls import path
from .views import get_quiz, index

urlpatterns = [
    path('', index, name='index'),
    path('api/get-quiz/', get_quiz, name='get_quiz'),
]
