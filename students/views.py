from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class StudentSignupView(CreateView):
    template_name = 'signup_student.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('questions')
