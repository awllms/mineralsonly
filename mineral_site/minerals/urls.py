from django.urls import path

from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('mineral/<pk>', views.mineral_detail, name='detail'),
]
