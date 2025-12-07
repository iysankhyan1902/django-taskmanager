from django.contrib import admin
from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView, CompletedTaskListView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(),name="task-home"),
    path('about/', views.task_about,name="task-about"),
    path('task/<int:pk>',TodoDetailView.as_view(),name="task-detail"),
    path('task/<int:pk>/complete/', views.mark_complete, name='task-complete'),
    path('task/new/', TodoCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TodoUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TodoDeleteView.as_view(), name='task-delete'),
    path("tasks/completed/", CompletedTaskListView.as_view(), name="completed-tasks"),


]