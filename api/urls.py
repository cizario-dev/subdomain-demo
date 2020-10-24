from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('showtime/', views.current_datetime),
]