from django.urls import path

from webapp.views import IndexView, CreateTask, TaskView, UpdateTask, DeleteTask
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('tasks/add/', CreateTask.as_view(), name="create_task"),
    path('article/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('task/<int:pk>/update', UpdateTask.as_view(), name="update_task"),
    path('task/<int:pk>/delete', DeleteTask.as_view(), name="delete_task"),
]