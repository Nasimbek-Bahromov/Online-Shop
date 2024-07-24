# list ---
# detail ---
# create ---
# update ---
# delete ---

from Goods import models
from django.shortcuts import render, redirect


def listProduct(request):
    queryset = models.Product.objects.all()
    context = {}
    context['queryset'] = queryset
    return render(request, 'back-office/product/list.html',context)


def detailProduct(request, id):
    queryset = models.Product.objects.get(id=id)
    context = {}
    print(models.ProductImg.objects.filter(product=queryset))
    context['queryset'] = queryset
    context['images'] = models.ProductImg.objects.filter(product=queryset)
    return render(request, 'back-office/product/detail.html',context)


def createProduct(request):
    context = {}
    context['categorys'] = models.Category.objects.all()
    if request.method == 'POST':
        # way 1
        # category_id = request.POST['category_id']
        # category = models.Category.objects.get(id=category_id)
        # product = models.Product.objects.create(
        #     name = request.POST['name'],
        #     quantity = request.POST['quantity'],
        #     price = request.POST['price'],
        #     category = category, 
        #     description = request.POST['description']
        # )
        # way 2
        product = models.Product.objects.create(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            price = request.POST['price'],
            category_id = request.POST['category_id'], 
            description = request.POST['description']
        )

        images = request.FILES.getlist('images')

        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )
    return render(request, 'back-office/product/create.html', context)


def deleteProduct(request, id):
    models.Product.objects.get(id=id).delete()
    return redirect('listProduct')