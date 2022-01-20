from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check_username')
]

urlpatterns += htmx_urlpatterns
