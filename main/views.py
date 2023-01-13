from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

# Create your views here.
class Singup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts/login/")
    template_name = "signup.html"


def home(request):
    return render(request, "base.html", {})
