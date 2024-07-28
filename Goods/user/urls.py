from django.urls import path
from . import views

urlpatterns = [
    path('mycart/', views.myCart, name='mycart'),
    path('add/<int:id>', views.addProductToCart, name='addToCart')
]