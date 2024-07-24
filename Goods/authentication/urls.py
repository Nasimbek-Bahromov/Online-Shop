from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.log_out, name='log_out'),
    path('error/', views.error, name='error')
]