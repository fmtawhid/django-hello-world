# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('', index, name='home'),
    path('contact', index, name='contact'),
    path('', index, name='home'),
    path('', index, name='home'),
]