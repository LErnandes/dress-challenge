from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")

def health(request):
    return HttpResponse()
