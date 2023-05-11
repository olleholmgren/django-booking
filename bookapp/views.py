from django.shortcuts import render, HttpResponse

def greet(request):
    return HttpResponse('Welcome!')