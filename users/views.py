from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import forms, models

class RegisterView(View):
    def get(self, request):
        form = forms.CustomRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users:user_list')
        return render(request, 'users/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = models.CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'
