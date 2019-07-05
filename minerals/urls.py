from django.urls import path

from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('detail/', views.mineral_detail, name='detail'),
]
