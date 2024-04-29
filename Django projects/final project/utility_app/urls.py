from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/',views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('home/currency_converter/', views.currency_converter, name='currency_converter'),
    path('home/calculator/', views.calculator_view, name='calculator'),
    path('logout/', logout_view, name='logout'),
    path('home/new_notepad/', views.new_notepad, name='new_notepad'),
    path('home/new_notepad/<int:pk>', views.open_notepad, name='open_notepad'),
    path('home/new_notepad/new/', views.create_note, name='create_note'),
    path('home/new_notepad/edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('home/new_notepad/delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('home/calculator/', views.calculator_view, name='calculator_view'),
    path('home/feedback/', views.feedback, name='feedback'),
    path('success/', views.feedback_success, name='feedback_success'),
]
