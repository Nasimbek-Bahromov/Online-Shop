# list +-+-
# detail +-+-
# create +-+-
# update +-+-
# delete +-+-

from django.shortcuts import render, redirect

from Goods import models


def listCategory(request):
    queryset = models.Category.objects.all()
    
    context = {}
    context['queryset'] = queryset

    return render(request, 'back-office/category/list.html', context)


def detailCategory(request, id):
    queryset = models.Category.objects.get(id=id)
    
    context = {}
    context['queryset'] = queryset

    return render(request, 'back-office/category/detail.html', context)


def createCategory(request):
    models.Category.objects.create(
        name=request.POST['name']
    )
    return redirect('listCategory')


def updateCategory(request, id):

    queryset = models.Category.objects.get(id=id)
    queryset.name = request.POST['name']
    queryset.save()

    return redirect('listCategory')


def deleteCategory(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('listCategory')