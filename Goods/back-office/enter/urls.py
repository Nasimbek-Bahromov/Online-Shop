from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listEnter, name='listEnter'),
    path('detail/<int:id>/', views.detailEnter, name='detailEnter'),
    path('update/<int:id>/', views.updateEnter, name='updateEnter'),
    path('delete/<int:id>/', views.deleteEnter, name='deleteEnter'),
    path('create', views.createEnter, name='createEnter'),   
]