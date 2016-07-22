from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Sesion
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from web.models import Document
from web.forms import DocumentForm

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


@csrf_exempt
def uploadFile(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('/')
        return HttpResponse("0")
    else:
        form = DocumentForm() # A empty, unbound form
        return HttpResponse("-1")

