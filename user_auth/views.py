from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View

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
            return redirect('Recipes:index')  # redirect to main page
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})


class UserLogin(View):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("Recipes:index")
        else:
            return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect("Recipes:index")
