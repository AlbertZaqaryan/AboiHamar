from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('category/<str:id>', views.CategoryListView.as_view(), name='home-detail'),

]