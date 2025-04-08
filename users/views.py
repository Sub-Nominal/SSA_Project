
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forms import TopUpForm


@login_required(login_url='users:login')
def user(request):
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse("users:user"))
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, "Invalid Credentials.")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('users:login')

from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def user_view(request):
    profile = request.user.profile  # Get the logged-in user's profile
    return render(request, 'users/user.html', {'balance': profile.balance}) #return the balance

def user(request):
    profile = request.user.profile
    return render(request, 'users/user.html', { #returns the user and their balance
        'user': request.user,
        'balance': profile.balance
        profile.balance += amount
        profile.save()
    })
context = {
    'form': form,
    'user_balance': request.user.profile.balance,
    'welcome_message': f"Welcome back, {request.user.first_name}!",
}
return render(request, 'chipin/top_up.html', context)
    

form = TopUpForm()
return render(request, 'users/top_up.html', {'form': form})
