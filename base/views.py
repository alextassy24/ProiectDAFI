import random
import time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import RegisterForm
from .models import SensorData


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
    min_val = 0
    max_val = 0
    data = SensorData.objects.filter(user=request.user)

    value = 0
    if request.user.is_authenticated:
        if request.method == 'POST':
            min_val = float(request.POST.get('minValue'))
            max_val = float(request.POST.get('maxValue'))
            value = round(random.uniform(min_val, max_val), 2)
            random_value = SensorData(user=request.user, value=value)
            random_value.save()
    context = {
        'data': data,
        'min_value': min_val,
        'max_value': max_val,
        'value': value}
    return render(request, 'view_data.html', context)
