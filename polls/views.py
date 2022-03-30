from django.shortcuts import render

# Create your views here.

#part1 Write your first view
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")