from django.urls import path
from .views import *
urlpatterns=[
    path('new/student/',StudentSignupView.as_view(),name='new_student')
]