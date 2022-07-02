from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
# Create your views here.
from webapp.forms import TaskForm
from webapp.models import Task, status_choices


def index_view(request):
    tasks = Task.objects.order_by("-done_at")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": status_choices})
    else:
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")
        done_at = request.POST.get("done_at")
        if done_at == "":
            done_at = None
        new_task = Task.objects.create(description=description, status=status, done_at=done_at, name=name)
        # context = {"task": new_task}
        return redirect("task_view", pk=new_task.pk)
        # return render(request, "index.html", context)


def task_view(request, **kwargs):
    pk = kwargs.get("pk")
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_view.html", {"task": task})
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound("Страница не найдена")
    #     raise Http404


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            "status": task.status,
            "name": task.name,
            "description": task.description
        })
        return render(request, "update.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.status = form.cleaned_data.get("status")
            task.author = form.cleaned_data.get("author")
            task.description = form.cleaned_data.get("description")
            task.save()
            return redirect("task_view", pk=task.pk)
        return render(request, "update.html", {"form": form})


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        pass
    #     return render(request, "delete.html", {"article": article})
    else:
        article.delete()
        return redirect("index")
