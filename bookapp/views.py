from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

def greet(request):
    return HttpResponse('Welcome!')