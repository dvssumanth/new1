from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dvs(request):
    return HttpResponse('<marquee><h1> you need to get a job</h1></marquee>')