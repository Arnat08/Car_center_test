from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from market.models import Car,Order
orders = []

cars = [
    {
        "id": 1,
        "available": 2,
        "model": "A7",
        "image": "https://thumb.tildacdn.com/tild3962-6335-4139-b962-386636356338/-/resize/312x/-/format/webp/2019.png"
    },
    {
        "id": 2,
        "available": 2,
        "model": "A8",
        "image": "https://thumb.tildacdn.com/tild3764-6131-4966-b237-393635633965/-/resize/312x/-/format/webp/2019.png"
    },
    {
        "id": 3,
        "available": 2,
        "model": "Q7",
        "image": "https://thumb.tildacdn.com/tild6639-3434-4839-b730-393630373130/-/resize/312x/-/format/webp/2020.png"
    },
    {
        "id": 4,
        "available": 2,
        "model": "A6",
        "image": "https://thumb.tildacdn.com/tild3836-3936-4134-a433-353663656330/-/resize/312x/-/format/webp/2019.png"
    },
    {
        "id": 5,
        "available": 2,
        "model": "S8",
        "image": "https://thumb.tildacdn.com/tild3764-3536-4039-a361-653430366464/-/resize/312x/-/format/webp/2020.png"
    },
]


def audi(request: HttpRequest) -> HttpResponse:
    global cars
    context = {"cars":cars,
               "name": "Arnat"
               }
    return render(request,"cars.html",context)




