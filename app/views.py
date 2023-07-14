from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic is inserted Successfully')

    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Webpage is inserted Successfull')
            
    return render(request,'insert_webpage.html',d)



def insert_access(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}

    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('AccessRecord is inserted Successfully')
            
    return render(request,'insert_access.html',d)