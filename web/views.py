from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Sesion

import hashlib
import time

@csrf_exempt
def index(request):
    return render(request, 'web/index.html')

@csrf_exempt
def cam(request):
    return render(request, 'web/cam.html')

@csrf_exempt
def linked(request):
    return render(request, 'web/linked.html')

@csrf_exempt
def new_token(request):
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode('utf-8'))
    return HttpResponse(hash.hexdigest())

@csrf_exempt
def registry_token(request):
    try:
        tk = request.COOKIES["cookie"]
        s = Sesion(token=tk)
        s.save()
    except:
        return HttpResponse("0")
    return HttpResponse("1")

@csrf_exempt
def is_registred(request):
    try:
        tk = request.COOKIES["cookie"]
        Sesion.objects.get(token=tk)
    except:
        return HttpResponse("0")

    return HttpResponse("1")

