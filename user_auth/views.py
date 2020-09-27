from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # redirect to main page
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})


def user_login(request):
    pass


def logout_view(request):
    logout(request)
    return redirect("Recipes:index")
