from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
# Create your views here.
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, ListView, DetailView, CreateView

from webapp.views.base_view import FormView as CustomFormView
from webapp.forms import TaskForm, SearchForm, ProjectForm
from webapp.models import Task, Project


class IndexViewProjects(ListView):
    model = Project
    template_name = "projects/index.html"
    context_object_name = "projects"
    ordering = "-updated_at"
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Project.objects.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return Project.objects.all()

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


class ProjectView(DetailView):
    template_name = "projects/project_view.html"
    model = Project
    context_object_name = "projects"
    ordering = "-updated_at"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.order_by("-created_at")
        return context


class CreateProject(CreateView):
    form_class = ProjectForm
    template_name = "projects/create.html"

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        form.save_m2m()
        return redirect("project_view", pk=project.pk)
