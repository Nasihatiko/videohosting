from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import RegistrationForm


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('video_list_url')
    success_message = 'Successfully registered'


class SignInView(LoginView):
    template_name = 'account/login.html'


# class ProfileView(DetailView):
#     model = User
#     template_name = 'account/profile.html'

# def profile(request):
#     return render(request, 'account/profile.html')


