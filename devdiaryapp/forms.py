# forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task", "description", "user", "due_date", "is_completed"]
