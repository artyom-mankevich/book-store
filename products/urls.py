from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
    path('<str:author>/<slug:slug>', views.ProductByIdView.as_view(), name='product detail'),
]
