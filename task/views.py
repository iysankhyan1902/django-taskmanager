from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task


def task_about(request):
    return render (request,"task/about.html")
class TodoListView(LoginRequiredMixin,ListView):
    model=Task
    template_name="task/task_list.html"
    fields = ["title","priority","is_completed"]
    context_object_name = "tasks"
    ordering="-created_at"
    paginate_by = 3

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)

        priority = self.request.GET.get("priority")

        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset


class CompletedTaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    fields = ["title", "priority", "is_completed"]
    context_object_name = "tasks"
    ordering = "-created_at"
    paginate_by = 3

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user,is_completed=True )


class TodoDetailView(DetailView):
    model=Task

def mark_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('task-detail', pk=pk)

class TodoCreateView(LoginRequiredMixin,CreateView):
    model=Task
    fields = ["title","description", "priority","is_completed"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Task
    fields = ["title","description", "priority","is_completed"]

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.owner:
            return True
        return False

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model=Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.owner:
            return True
        return False




