from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# hexlet_django_blog/article/views.py


def index(request):
    return HttpResponse("article")
