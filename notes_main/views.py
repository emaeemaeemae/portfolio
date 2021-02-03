from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import UserLoginForm, RegisterUserForm


def index(request):
    return render(request, 'notes_main/index.html')


def contacts(request):
    return render(request, 'notes_main/contacts.html')


class UserLoginView(LoginView):
    template_name = 'notes_main/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('notes_home')

    def get_success_url(self):
        return self.success_url


class UserLogout(LogoutView):
    next_page = 'notes_main'


class RegisterUserView(CreateView):
    model = User
    template_name = 'notes_main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('notes_home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid
