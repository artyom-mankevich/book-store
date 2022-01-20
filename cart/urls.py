from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    path('update_item/', views.update_item, name='update_item'),
    path('save_order/', views.save_order, name='save_order')
]