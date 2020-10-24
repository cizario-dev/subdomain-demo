from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index),
    path('foo/2003/', views.foo_2003),
    path('foo/<int:year>/', views.foo_bar),
]