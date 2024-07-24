from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.all()
    category = models.Category.objects.all()
    
    context = {}
    context['banners'] = banners
    context['categories'] = category

    return render(request, 'index.html', context)


def user(request):
    return render(request, 'user.html')
