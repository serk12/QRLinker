from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def cam(request):
    return render(request, 'web/cam.html')