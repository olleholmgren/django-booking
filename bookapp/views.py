from django.shortcuts import render


def show_car(request):
    return render(request, 'car_fleet/index.html')

def sign_up_page(request):
    return render(request, 'car_fleet/signup.html')