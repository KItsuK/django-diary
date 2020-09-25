from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreatForm
from .models import Day

class IndexView(generic.ListView):
    model = Day
    paginate_by = 10 #一ページに何件表示するか

class AddView(generic.CreateView):
    model = Day
    form_class = DayCreatForm
    success_url = reverse_lazy('diary:index')

class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreatForm
    success_url = reverse_lazy('diary:index')

class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day
