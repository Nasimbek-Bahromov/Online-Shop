from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createProduct, name='createProduct'),
    path('list', views.listProduct, name='listProduct'),
    path('detail/<int:id>/', views.detailProduct, name='detailProduct'),
    path('delete/<int:id>/', views.deleteProduct, name='deleteProduct')
]