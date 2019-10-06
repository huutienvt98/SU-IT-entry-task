from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from signup.forms import CustomUserCreationForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(data = request.POST)
        if f.is_valid():
            user = f.save()
            username = f.cleaned_data.get('username')
            raw_password = f.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('login')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'signup.html', {'form': f})