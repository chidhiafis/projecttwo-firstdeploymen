from django.urls import path
from .views import *

urlpatterns=[
    path('questions',QuestionListView.as_view(),name='questions'),
    path('question/new/',NewQuestion.as_view(),name='new_question')
]