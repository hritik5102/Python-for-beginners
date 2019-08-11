from django.shortcuts import render
from django.http import HttpResponse

# it takes a request and send to view function
def index(request) :
    return HttpResponse('Hellow world')
    
    
