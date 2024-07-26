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
  # Fetch the category object
  vegi = models.Category.objects.get(id=id)
  print(f' vegi: {vegi}')

  context = {
      'vegi': vegi
  }

  if request.method == 'POST':
    vegi.name = request.POST['name']
    print(f' Updated data.name: {vegi.name}')

    vegi.save()

  return render(request, 'back-office/category/update.html', context)



def deleteCategory(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('listCategory')