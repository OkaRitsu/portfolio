from django.urls import path
from django.views.generic.base import View

from . import views


app_name = 'products'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product-list/', views.ProductListView.as_view(), name='product_list')
]
