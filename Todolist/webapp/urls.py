from django.urls import path

from webapp.views import IndexView, CreateTask, TaskView, UpdateTask, DeleteTask, IndexViewProjects, CreateProject, \
    ProjectView

urlpatterns = [
    path('', IndexViewProjects.as_view(), name="index_project"),
    path('projects/add/', CreateProject.as_view(), name="create_project"),
    path('project/<int:pk>/', ProjectView.as_view(), name="project_view"),
    path('tasks/', IndexView.as_view(), name="index"),
    path('tasks/add/', CreateTask.as_view(), name="create_task"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('task/<int:pk>/update', UpdateTask.as_view(), name="update_task"),
    path('task/<int:pk>/delete', DeleteTask.as_view(), name="delete_task"),
]
