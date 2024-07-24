from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listCategory, name='listCategory'),
    path('detail/<int:id>/', views.detailCategory, name='detailCategory'),
    path('update/<int:id>/', views.updateCategory, name='updateCategory'),
    path('delete/<int:id>/', views.deleteCategory, name='deleteCategory'),
    path('create', views.createCategory, name='createCategory'),
]