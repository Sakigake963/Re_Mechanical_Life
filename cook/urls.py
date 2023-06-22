from django.urls import path
from . import views

urlpatterns = [
    path('cook/', views.meal_suggestion, name='meal_suggestion'),
    path('receive_data/', views.receive_data, name='receive_data'),
]