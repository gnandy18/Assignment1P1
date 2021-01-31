from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    path('req_new', views.req_new, name='req_new'),
    url(r'^password/$', views.change_password, name='change_password'),

    path('req_new/create/', views.req_new, name='req_new'),
    path('req_list', views.req_list, name='req_list'),
    path('req_delete/<int:pk>/', views.req_delete, name='req_delete'),
    path('req_edit/<int:pk>/edit/', views.req_edit, name='req_edit'),
    path('admin_req_list', views.admin_req_list, name='admin_req_list'),
    path('req_approve/<int:pk>/', views.req_approve, name='req_approve'),
    path('req_delivered/<int:pk>/', views.req_delivered, name='req_delivered'),
    path('item_list', views.item_list, name='item_list'),
    path('item_new/create/', views.item_new, name='item_new'),
    path('item_delete/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('item_edit/<int:pk>/edit/', views.item_edit, name='item_edit'),


]
