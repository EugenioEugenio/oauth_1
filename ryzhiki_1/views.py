
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterUserForm

# ВОТ ЭТОТ КЛАСС ДОЛЖЕН БЫТЬ ТУТ:
class HomeView(TemplateView):
    template_name = 'ryzhiki_1/home.html'

class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'ryzhiki_1/register.html'
    success_url = reverse_lazy('login')

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'ryzhiki_1/protected.html'

