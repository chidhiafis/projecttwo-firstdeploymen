from django import forms
from .models import Question
from django.contrib.auth import get_user_model
class NewQuestionForm(forms.ModelForm):
    user=forms.ModelChoiceField(widget=forms.HiddenInput,queryset=get_user_model().objects.all(),disabled=True)
    class Meta:
        model=Question
        fields=['title','body','user']