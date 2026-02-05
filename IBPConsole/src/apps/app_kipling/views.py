from django.shortcuts import render
from django.http import HttpResponse

def index(self):
    """
    Docstring for index
    """
    return HttpResponse("Welcome BFF OptiPrice!")
