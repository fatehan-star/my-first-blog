from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return(HttpResponse("START project"))

# Create your views here.
