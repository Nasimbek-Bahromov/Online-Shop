from django.core.paginator import Paginator
from django.shortcuts import render
from . import models

def main(request):
    banners = models.Banner.objects.all()
    categories = models.Category.objects.all()
    last_img = models.ProductImg.objects.all()
    infos = models.Info.objects.last()
    products = models.Product.objects.all()
    wishlist = models.WishList.objects.all()

    # Pagination
    paginator = Paginator(last_img, 4)  # 4 ta maxsulotlarni pagination qildim
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'banners': banners,
        'categories': categories,
        'products': last_img,
        'info': infos,
        'page_obj': page_obj,
        'wishlist': wishlist,
    }

    return render(request, 'index.html', context)



def user(request):
    return render(request, 'user/detail.html')


