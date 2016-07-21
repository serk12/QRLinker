from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'web/index.html')

def cam(request):
    return render(request, 'web/cam.html')

def linked(request):
    return render(request, 'web/linked.html')

def new_token(request):
    return HttpResponse("Dummy token")