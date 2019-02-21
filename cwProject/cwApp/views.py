from django.shortcuts import HttpResponse
from .models import Book
from .models import Car


# basic index test message
def index(request):
    return HttpResponse('this is the index page')


# new book function call by the newbook path (creates a new book)
def new(request):
    bookModel = Book.objects.all()
    newBook = Book(name='Hate', pageNumber=150, publishDate='2017-02-05', genre='Romance')
    newBook.save()
    return HttpResponse(bookModel)


# all book function called by the all path (lists all book names)
def all(request):
    bookModel = Book.objects.all()
    return HttpResponse('Book 1: ' + str(bookModel[0]) + ' Book 2:' + str(bookModel[1]))


# janDate function called by the janDate path (lists all book names published after Jan 2018)
def janDate(request):
    newBooks = Book.objects.filter(publishDate__gt='2018-01-01')
    return HttpResponse(newBooks)


# car all function called by callAll path (lists all cars in the model)
def carAll(request):
    carModel = Car.objects.all()
    return HttpResponse('Car 1: ' + str(carModel[0]) + ' Car 2:' + str(carModel[1]))


# new car function called by the newCar path (adds a car to the model)
def newCar(request):
    carModel = Car.objects.all()
    newCar = Car(make='Honda', model='Civic', year='2017-02-05')
    newCar.save()
    return HttpResponse(carModel)


# oldCar function called by the oldCar path (lists all cars made after 2010 with a misleading name)
def oldCar(request):
    oldCar = Car.objects.filter(year__gt='2010-01-01')
    return HttpResponse(oldCar)
