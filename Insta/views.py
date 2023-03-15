from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Snap(request):
    return HttpResponse('<h1>Take a Snap</h1>')

def Message(request):
    return HttpResponse('<marquee><h1>Ⓜ️essege Sent Succesfully😊</h1></marquee>')