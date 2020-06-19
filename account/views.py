from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import RegisterForm
from account.mixins import LoggedInRedirectMixin

class Login(LoggedInRedirectMixin, LoginView):
    pass

class Logout(LoginRequiredMixin, LogoutView):
    pass

class Register(LoggedInRedirectMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('gallery:login')