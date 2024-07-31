from django.urls import path
from . import views

urlpatterns = [
    path('mycart/', views.myCart, name='mycart'),
    path('add/<int:id>/', views.addProductToCart, name='addToCart'),
    path('substract/<int:id>/', views.substruct, name='substract'),
    path('delete/<int:id>/', views.deleteProductCart, name='delete'),
    path('order/<int:id>/', views.CreateOrder, name='createOrder'),
    path('wishlist/', views.wishList, name='wishList'),
    path('addOrDelete/<int:id>/', views.addOrDeleteWishList, name='addOrDelete')

]