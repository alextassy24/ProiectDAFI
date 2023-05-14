import csv
from django.http import HttpResponse
import random
import time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import RegisterForm
from .models import Temperature, Pressure


def home(request):
    return render(request, 'home.html')


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'User {username} does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f'Username or password are incorrect!')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'register.html', {'form': form})


def view_data(request):
    context = {}

    if request.user.is_authenticated:
        temp_data = Temperature.objects.all()
        press_data = Pressure.objects.all()

        # if request.method == 'POST':
        #     min_val = float(request.POST.get('minValue'))
        #     max_val = float(request.POST.get('maxValue'))
        #     value = round(random.uniform(min_val - 5, max_val + 5), 2)
        #     random_value = Temperature(user=request.user, value=value)
        #     random_value.save()

        # if value == min_val:
        #     messages.warning(
        #         request, 'The teampeature is near the lower limit')
        # elif value == max_val:
        #     messages.warning(
        #         request, 'The teampeature is near the higher limit')
        # elif value < min_val:
        #     messages.error(
        #         request, 'The teampeature is under the lower limit')
        # elif value > max_val:
        #     messages.error(
        #         request, 'The teampeature is beyond the higher limit')
        # else:
        #     messages.success(request, 'The temperature is perfect!')
    context = {
        'temp_data': temp_data,
        'press_data': press_data
    }
    return render(request, 'view_data.html', context)


def download_temperature(request):
    data = Temperature.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="temperature.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Value'])
    for datapoint in data:
        writer.writerow([datapoint.id, datapoint.timestamp, datapoint.value])

    return response


def download_pressure(request):
    data = Pressure.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Pressure.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Value'])
    for datapoint in data:
        writer.writerow([datapoint.id, datapoint.timestamp, datapoint.value])

    return response
