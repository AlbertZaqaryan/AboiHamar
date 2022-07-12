from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Prod, Brand
# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cats = Category.objects.all()
        return render(request, self.template_name, {'cats':cats})

class BrandListView(ListView):
    template_name = 'brand.html'

    def get(self, request, id):
        brands = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'brands':brands})


class CategoryListView(ListView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        category = Brand.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'category':category})

class CategoryDetailView(DetailView):
    template_name = 'home_detail_detail.html'

    def get(self, request, id):
        prod = Prod.objects.get(pk=id)
        return render(request, self.template_name, {'prod':prod})
