from django.contrib import messages
from django.contrib.auth import login
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
