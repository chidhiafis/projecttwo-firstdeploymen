from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Question
from .forms import NewQuestionForm
from django.urls import reverse_lazy


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = "question_list.html"
    context_object_name = "questions"


class NewQuestion(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = NewQuestionForm
    success_url = reverse_lazy("questions")
    template_name = "new_question.html"
    permission_required = "qna.add_question"

    def get_initial(self):
        return {"user": self.request.user.id}
