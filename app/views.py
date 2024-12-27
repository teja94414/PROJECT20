from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_Topic(request):
    tn=input("Enter Topic_name")
    TOD=Topic .objects.get_or_create(topic_name=tn)
    if TOD[1]:
        return HttpResponse("New topic is created")
    else:
        return HttpResponse("Given Topic is a already present")
    
    
    
def insert_webpage(request):
        tn=input('Enter Topic_name')
        n=input('Enter Name')
        url=input('Enter Url')
        email=input('Enter Email')
        LTO=Topic.objects.filter(topic_name=tn)
        if LTO:
            WTOD=Webpage.objects.get_or_create(topic_name=LTO[0],name=n,Url=Url,email=email)
            if WTOD[1]:
                return HttpResponse("Web is Created")
            else:
                return HttpResponse("Web is present")
        else:
            return HttpResponse("Given topic is not present")

def insert_access(request):
        pk=int(input('Enter pk of webpage'))
        author=input('Enter author')
        date=input('Enter date')
        LWO=Webpage.objects.filter(pk=pk)
        if LWO:
            WO=LWO[0]
            ATOD=AccessRecord.objects.get_or_create(name=WO,author=author,date=date,)
            if ATOD[1]:
                return HttpResponse("New Access is created")
            else:
                return HttpResponse("With Given Details Access is Already Present")
        else:
            return HttpResponse("Given parent Webpage Table Data is not present in DB")
