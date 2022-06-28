from django.urls import path

from webapp.views import index_view, create_task
urlpatterns = [
    path('', index_view, name="index"),
    path('tasks/add/', create_task, name="create_task"),
]