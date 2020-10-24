from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('greeting/<str:name>', views.greetings ),
    path('contacts', views.get_contacts),
]