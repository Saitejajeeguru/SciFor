from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name="quiz"),
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
    path('quiz/', views.quiz_page, name='quiz_page')
]

