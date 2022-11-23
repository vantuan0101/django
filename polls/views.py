from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Feature
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
    # name = "Beo ne"
    context = {
        'name' : 'Beo ne',
        'age' : 20,
        'address' : 'Ha Noi',
    }
    # feature = Feature()
    # feature.id =1 
    # feature.name = 'Feature 1'
    # feature.details = 'Feature 1 details'
    feature = Feature.objects.all()
    return render(request , 'index.html' , context ) # {'name':name}

def counter(request):
    text = request.POST['text']
    return render(request , 'counter.html' , {'text':text})

def posts(request , id) :
    return render(request , 'post.html' , {'id':id})