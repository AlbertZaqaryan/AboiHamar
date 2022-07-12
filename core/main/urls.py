from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('brand/<str:id>', views.BrandListView.as_view(), name='brand'),
    path('category/<str:id>', views.CategoryListView.as_view(), name='home_detail'),

]