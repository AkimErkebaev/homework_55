from django.shortcuts import render
# Create your views here.
from webapp.models import Task, status_choices


def index_view(request):
    tasks = Task.objects.order_by("-done_at")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": status_choices})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        done_at = request.POST.get("done_at")
        new_task = Task.objects.create(description=description, status=status, done_at=done_at)
        context = {"task": new_task}
        return render(request, "index.html", context)
