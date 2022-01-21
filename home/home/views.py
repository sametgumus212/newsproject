from django.shortcuts import render,HttpResponse
from newsfetch.google import google_search
from home.home.models import Venue
from django.http import HttpResponse
import csv
from templates import *

def venue_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="venue_csv"'
    #create a csv writer
    writer=csv.writer(response)


    venues=Venue.objects.all()

    #Add column headings to the csv file
    writer.writerow(['links'])

    # lines=[]
    for venue in venues:
        writer.writerow([venue.link])
    return response


def home_view(request):
    data=request.POST.get('name')
    return render(request,'home.html',{'data':data})

def add(request):
    num1=request.GET.get("num1")
    num2=request.GET.get("num2")
    fname=request.GET.get("fname")
    if num1!=None and num2!=None:
        google=google_search(num1, num2,fname)
        for i in google.urls:
            result=i
    else:
        pass
    return render(request,'result.html',{"result":result})