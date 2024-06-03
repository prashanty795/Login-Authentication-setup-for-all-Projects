from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def user_login(request):
    user = request.user
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, "Your account is disabled")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'homecover.html')

@login_required
def dashboard(request):
    return render(request, 'organization/admin_dashboard.html', {'section': 'dashboard'})       

@login_required
def create_organization(request):
    return render(request, 'organization/create_organization.html', {'section': 'dashboard'})       