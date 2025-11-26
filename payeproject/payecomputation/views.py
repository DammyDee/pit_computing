from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})