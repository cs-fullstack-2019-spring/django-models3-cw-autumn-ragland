from django.urls import path
from . import views
# paths that call functions
urlpatterns = [
    path('', views.index, name='index'),
    # books
    path('newbook/', views.new, name='new book'),
    path('all/', views.all, name='all books'),
    path('janDate/', views.janDate, name='publish last year'),
    # cars
    path('carAll/', views.carAll, name='all cars'),
    path('newCar/', views.newCar, name='add a car'),
    path('oldCar/', views.oldCar, name='list older models')
]
