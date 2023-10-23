from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "index.html.html")

def new(request):
    return render(request, "game_record.html" )