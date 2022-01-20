import re

from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_pic = form.cleaned_data.get('profile_pic')
            user.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}')
            return redirect('store:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def check_username(request):
    username = request.POST.get('username')
    if not re.match("^[a-z0-9_]{3,30}$", username):
        return HttpResponse("<div id='username-errors'></div>")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-errors' class='invalid'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-errors' class='valid'>This username is available</div>")
