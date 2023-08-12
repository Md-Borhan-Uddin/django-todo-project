from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, DetailView
from django.shortcuts import redirect, render
from todo.forms import TodoCreateForm

from todo.models import TodoModel

# Create your views here.


class TodoListView(ListView):
    model = TodoModel
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = TodoModel.objects.filter(is_completed=False)
        return context


class TodoCompleteView(ListView):
    model = TodoModel
    template_name = 'todo/complete.html'
    context_object_name = 'todo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = TodoModel.objects.filter(is_completed=True)
        return context


class TodoDetailView(DetailView):
    model = TodoModel
    template_name = 'todo/single_todo.html'
    context_object_name = 'todo'

class TodoDeleteView(DeleteView):
    model = TodoModel
    template_name = 'todo/delete_todo.html'
    success_url = reverse_lazy('show_todo')

class TodoCreateView(CreateView):
    model = TodoModel
    template_name = "todo/create.html"
    form_class = TodoCreateForm


class TodoUpdateView(UpdateView):
    model = TodoModel
    template_name = "todo/update.html"
    form_class = TodoCreateForm



def update_completed(request,id):
    todo = TodoModel.objects.get(id=id)
    todo.is_completed = True
    todo.save()
    return redirect(reverse_lazy('show_todo_complete'))