from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert(request):
    TO=Topicform()
    WO=Webpageform()
    AO=Accessrecordform()
    d={'TO':TO,'WO':WO,'AO':AO}
    if request.method=='POST':
        TOD=Topicform(request.POST)
        WOD=Webpageform(request.POST)
        AOD=Accessrecordform(request.POST)
        if TOD.is_valid() and WOD.is_valid() and AOD.is_valid():
            NSTO=TOD.save(commit=False)
            NSTO.save()
            NSWO=WOD.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()
            NSAO=AOD.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('data is saved succssully')
        else:
            return HttpResponse('data is not saved')

    
    return render(request,'insert.html',d)