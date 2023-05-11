from django.shortcuts import render


def show_car(request):
    return render(request, 'car_fleet/index.html')