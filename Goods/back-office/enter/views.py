from django.shortcuts import render, redirect

from Goods import models


def listEnter(request):
    queryset = models.ProductEnter.objects.all()
    context = {}
    context['queryset'] = queryset

    return render(request, 'back-office/enter/list.html', context)


def detailEnter(request, id):
    queryset = models.ProductEnter.objects.get(id=id)
    context = {}
    context['queryset'] = queryset

    return render(request, 'back-office/enter/detail.html', context)


def createEnter(request):
    product = models.Product.objects.all()
    context = {}
    context['products'] = product


    if request.method == 'POST':
        models.ProductEnter.objects.create(
            product_id = request.POST['product_id'],
            quantity = request.POST['number'],
            date = request.POST['date'],
            description = request.POST['description'],
        )
        
    return render(request, 'back-office/enter/create.html', context)


def updateEnter(request, id):
    vegi = models.ProductEnter.objects.get(id=id)

    context = {
        'data': vegi
    }

    if request.method == 'POST':
        vegi.product.name = request.POST['name']
        vegi.quantity = request.POST['quantity']
        vegi.description = request.POST['description']
        vegi.save()
        return redirect('listEnter')
    return render(request, 'back-office/enter/update.html', context)



def deleteEnter(request, id):
    models.ProductEnter.objects.get(id=id).delete()
    return redirect('listEnter')