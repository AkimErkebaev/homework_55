from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView

from webapp.base_view import FormView as CustomFormView
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


class CreateTask(CustomFormView):
    form_class = TaskForm
    template_name = "create.html"

    def form_valid(self, form):
        # tags = form.cleaned_data.pop("tags")
        # self.article = Article.objects.create(**form.cleaned_data)
        # self.article.tags.set(tags)
        self.task = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect("task_view", pk=self.task.pk)


class UpdateTask(FormView):
    form_class = TaskForm
    template_name = "update.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("task_view", kwargs={"pk": self.task.pk})

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['instance'] = self.task
        return form_kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))


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
