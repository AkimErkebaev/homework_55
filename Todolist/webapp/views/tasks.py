from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, UpdateView, DeleteView

from webapp.views.base_view import FormView as CustomFormView
from webapp.forms import TaskForm, SearchForm, TaskDeleteForm
from webapp.models import Task, Project


class IndexView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = "-updated_at"
    paginate_by = 5
    permission_required = "webapp.view_task"

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Task.objects.filter(
                Q(name__icontains=self.search_value))
        return Task.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})  # search=dcsdvsdvsd
            context['query'] = query
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class TaskView(PermissionRequiredMixin, TemplateView):
    model = Task
    template_name = "tasks/task_view.html"
    permission_required = "webapp.view_task"
    context_object_name = "tasks"

    def has_permission(self):
        return super().has_permission()

    # extra_context = {"test": "test"}
    # def get_template_names(self):
    #     return "article_view.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)


class CreateTask(PermissionRequiredMixin, CustomFormView):
    form_class = TaskForm
    template_name = "tasks/create.html"
    permission_required = "webapp.change_task"

    def has_permission(self):
        return super().has_permission()

    def form_valid(self, form):
        # tags = form.cleaned_data.pop("tags")
        # self.article = Article.objects.create(**form.cleaned_data)
        # self.article.tags.set(tags)
        self.task = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect("webapp:task_view", pk=self.task.pk)


class UpdateTask(PermissionRequiredMixin, UpdateView):
    form_class = TaskForm
    template_name = "tasks/update.html"
    model = Task
    permission_required = "webapp.change_task"

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    # def dispatch(self, request, *args, **kwargs):
    #     self.task = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def get_success_url(self):
    #     return reverse("task_view", kwargs={"pk": self.task.pk})
    #
    # def get_form_kwargs(self):
    #     form_kwargs = super().get_form_kwargs()
    #     form_kwargs['instance'] = self.task
    #     return form_kwargs
    #
    # def form_valid(self, form):
    #     self.task = form.save()
    #     return super().form_valid(form)
    #
    # def get_object(self):
    #     return get_object_or_404(Task, pk=self.kwargs.get("pk"))


class DeleteTask(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = TaskDeleteForm
    permission_required = "webapp.delete_task"

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=self.get_object())
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)
