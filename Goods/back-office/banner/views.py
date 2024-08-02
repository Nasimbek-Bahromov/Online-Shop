from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Goods.models import Banner

class BannerListView(ListView):
    queryset = Banner.objects.all
    template_name = 'back-office/banners/banner_list.html'
    context_object_name = 'banners'

class BannerDetailView(DetailView):
    model = Banner
    template_name = 'back-office/banners/banner_detail.html'
    context = 'banner'

class BannerCreateView(CreateView):
    model = Banner
    template_name = 'back-office/banners/banner_update.html'
    fields = ['title', 'sub_title', 'img', 'is_active']
    success_url = reverse_lazy('banner-list')

class BannerUpdateView(UpdateView):
    model = Banner
    template_name = 'back-office/banners/banner_update.html'
    fields = ['title', 'sub_title', 'img', 'is_active']
    success_url = reverse_lazy('banner-list')

class BannerDeleteView(DeleteView):
    model = Banner
    template_name = 'back-office/banners/banner_delete.html'
    success_url = reverse_lazy('banner-list')
