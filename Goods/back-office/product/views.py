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
    print('queryset',queryset )
    print('id', id)
    querysetImg = models.ProductImg.objects.filter(product_id = id)
    context = {}
    context['queryset'] = queryset
    context['querysetImg'] = querysetImg
    context['images'] = models.ProductImg.objects.filter(product=queryset)
    return render(request, 'back-office/product/detail.html',context)


def createProduct(request):
    context = {}
    context['categorys'] = models.Category.objects.all()
    if request.method == 'POST':
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
        return redirect('listProduct')
    return render(request, 'back-office/product/create.html', context)


def deleteProduct(request, id):
    models.Product.objects.get(id=id).delete()
    return redirect('listProduct')

def updateProduct(request, id):
    data = models.Product.objects.get(id=id)

    context = {
        'data': data
    }

    if request.method == 'POST':
        data.name = request.POST['name']
        data.quantity = request.POST['quantity']
        data.price = request.POST['price']
        data.category.id = request.POST['category_id']
        data.description = request.POST['description']
        data.save()
        return redirect('listProduct')
    return render(request, 'back-office/product/update.html', context)