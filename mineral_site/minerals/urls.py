from django.urls import path

from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('mineral/<pk>', views.mineral_detail, name='detail'),
    path('search/<letter>', views.letter_search, name='letter_search'),
    path('search/', views.search, name='search'),
    path('group/<group>', views.group_search, name='group_search'),
]
