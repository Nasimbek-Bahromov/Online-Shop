from django.urls import path
from .views import BannerListView, BannerDetailView, BannerCreateView, BannerUpdateView, BannerDeleteView

urlpatterns = [
    path('list/',BannerListView.as_view(), name='banner-list'),
    path('detail/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),
    path('create/', BannerCreateView.as_view(), name='banner-create'),
    path('update/<int:pk>/', BannerUpdateView.as_view(), name='banner-update'),
    path('delete/<int:pk>/', BannerDeleteView.as_view(), name='banner-delete'),
]
