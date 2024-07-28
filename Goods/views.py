from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.all()
    category = models.Category.objects.all()
    last_img = models.ProductImg.objects.all()
    
    context = {}
    context['banners'] = banners
    context['categories'] = category
    context['products'] = last_img


    return render(request, 'index.html', context)


def user(request):
    return render(request, 'user/detail.html')
