from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, FormView
from cars.models import Car, Make

# Create your views here.
class IndexView(TemplateView):
    template_name = 'cars/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.filter(featured=True)
        context['makes'] = Make.objects.all()
        return context

class CarDetailView(DetailView):
    template_name = 'cars/detail.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = get_object_or_404(Car, pk=self.kwargs['pk'])
        context['recommended_cars'] = Car.objects.filter(make=car.make)[:3]
        return context