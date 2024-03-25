from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def home(request):
    return render(request,'home.html')
class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'usercreate.html'
    success_url = reverse_lazy('questions')