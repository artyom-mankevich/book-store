from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
    path('authors/<slug:slug>', views.AuthorDetails.as_view(), name='author details'),
    path('<slug:author>/<slug:slug>', views.ProductDetails.as_view(), name='product details'),
    path('<slug:slug>', views.PublisherDetails.as_view(), name='publisher details')
]
