from django.shortcuts import (render, redirect)
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Task
from .forms import CustomUserCreationForm, CustomAuthenticationForm, TaskForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('task')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    active_tab = 'all'
    return render(request, 'task.html', {'tasks': tasks, 'active_tab': active_tab})


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user.date_login = timezone.now()
            login(request, user)
            return redirect('tasks')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
