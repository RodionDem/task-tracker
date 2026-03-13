from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task-list")
