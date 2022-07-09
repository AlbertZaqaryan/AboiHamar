from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Prod
# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cats = Category.objects.all()
        return render(request, self.template_name, {'cats':cats})

class CategoryListView(ListView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        category = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'category':category})
