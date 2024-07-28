from django.shortcuts import render, redirect
from Goods import models


def myCart(request):
    cart = models.Cart.objects.get(author=request.user, is_active=True)
    cartProduct = models.CartProduct.objects.filter(cart= cart)
    context = {}
    context['cart']=cart
    context['cartpro']=cartProduct
    return render(request, 'user/detail.html', context)


def addProductToCart(request, id):
    product_id = id
    quantity = int(request.POST['quantity'])  # Convert quantity to integer
    product = models.Product.objects.get(id=product_id)
    cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
    try:
        cart_product = models.CartProduct.objects.get(cart=cart, product_id=product_id)
        cart_product.quantity += quantity
        cart_product.save()
    except models.CartProduct.DoesNotExist:
        cart_product = models.CartProduct.objects.create(
            product=product, 
            cart=cart,
            quantity=quantity
        )
    if quantity and product.price:
        cart_product.total_price = quantity * float(product.price)
        cart_product.save()
    return redirect('mycart')



def substruct(request, id):
    code = id
    quantity = int(request.POST['quantity'])
    product_cart = models.CartProduct.objects.get(id=code)
    product_cart.quantity = quantity
    product_cart.save()
    if not product_cart.quantity:
        product_cart.delete()
    return redirect('mycart')



def deleteProductCart(request, id):
    product_cart = models.CartProduct.objects.get(id=id)
    product_cart.delete()
    return redirect('mycart')


def CreateOrder(request, id):
    print('boshi')
    cart = models.Cart.objects.get(id=id)
    
    cart_products = models.CartProduct.objects.filter(cart=cart)

    done_products = []

    for cart_product in cart_products:
        if cart_product.quantity <= cart_product.product.quantity:
            cart_product.product.quantity -= cart_product.quantity
            cart_product.product.save()
            done_products.append(cart_product)
        else:
            for product in done_products:
                product.product.quantity += product.quantity
                product.product.save()
            raise ValueError('Qoldiqda kamchilik')
    if request.method == 'POST':
        models.Order.objects.create(
            cart_id=cart.id,
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            address = request.POST['address'],
            status = 1
            )
        cart.is_active = False
        cart.save()
        return render(request, 'user/order.html')
    return redirect('mycart')