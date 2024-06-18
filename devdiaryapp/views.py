from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task
from .forms import TaskForm


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, "devdiaryapp/home.html")


class RegisterPageView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/register.html", context)

    def post(self, request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not password1 or not password2:
            return redirect("/accounts/register/")

        if not password1 == password2:
            return redirect("/accounts/register/")

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/accounts/register/")


class TaskListView(ListView):
    model = Task
    template_name = "devdiaryapp/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "devdiaryapp/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "devdiaryapp/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "devdiaryapp/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "devdiaryapp/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")
