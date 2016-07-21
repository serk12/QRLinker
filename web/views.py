from django.shortcuts import render
from django.http import HttpResponse

import hashlib
import time


def index(request):
    return render(request, 'web/index.html')

def cam(request):
    return render(request, 'web/cam.html')

def linked(request):
    return render(request, 'web/linked.html')

def new_token(request):
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode('utf-8'))
    return HttpResponse(hash.hexdigest())