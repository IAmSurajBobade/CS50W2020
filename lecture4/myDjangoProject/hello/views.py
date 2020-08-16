from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(requrest):
    return render(requrest, "hello/index.html")


def greet(requrest, name):
    return render(requrest, "hello/greet.html", {
        "name": name.capitalize()
    })
