from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    print("This line is added at 21:52 04-12-2024")
    return HttpResponse('<h2>Hello, Students. Welcome to Django tutorials.</h2>')