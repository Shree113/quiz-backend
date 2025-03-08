from django.urls import path
from .views import get_questions, submit_score, leaderboard

urlpatterns = [
    path('', get_questions, name='get_questions'),
    path('submit/', submit_score, name='submit_score'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]
