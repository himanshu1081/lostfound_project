from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('lost', views.lost_list, name='lost_list'),
    path('found', views.found_list, name='found_list'),
    path('add-lost', views.add_lost, name='add_lost'),
    path('add-found', views.add_found, name='add_found'),
    path('lost/<int:id>/', views.lost_detail, name='lost_detail'),
    path('found/<int:id>/', views.found_detail, name='found_detail'),
    path('resolve-lost/<int:id>/', views.resolve_lost, name='resolve_lost'),
    path('resolve-found/<int:id>/', views.resolve_found, name='resolve_found'),
]
