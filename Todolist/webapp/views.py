from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task, Status, Type


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        tasks = Task.objects.order_by("-updated_at")
        kwargs["tasks"] = tasks
        return super().get_context_data(**kwargs)


class TaskView(TemplateView):
    template_name = "task_view.html"

    # extra_context = {"test": "test"}
    # def get_template_names(self):
    #     return "article_view.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)


class CreateTask(View):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = TaskForm()
            return render(request, "create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            description = request.POST.get("description")
            status = request.POST.get("status")
            status = Status.objects.get(id=status)
            type = request.POST.get("type")
            type = Type.objects.get(id=type)
            new_task = Task.objects.create(description=description, status=status, type=type,
                                           name=name)
            return redirect("task_view", pk=new_task.pk)
        return render(request, "create.html", {"form": form})
        # context = {"task": new_task}


class UpdateTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = TaskForm(initial={
                "status": self.task.status,
                "name": self.task.name,
                "description": self.task.description,
                "type": self.task.type
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            self.task.name = form.cleaned_data.get("name")
            self.task.description = form.cleaned_data.get("description")
            self.task.status = form.cleaned_data.get("status")
            self.task.type = form.cleaned_data.get("type")
            self.task.save()
            return redirect("task_view", pk=self.task.pk)
        return render(request, "update.html", {"form": form})


class DeleteTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            pass

    def post(self, request, *args, **kwargs):
        self.task.delete()
        return redirect("index")
