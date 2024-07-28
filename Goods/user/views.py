from django.shortcuts import render, redirect
from Goods import models


def myCart(request):
    cart = models.Cart.objects.get(author=request.user, is_active=True)
    cartProduct = models.CartProduct.objects.all()
    context = {}
    context['cart']=cart
    context['cartpro']=cartProduct
    return render(request, 'user/detail.html', context)


def addProductToCart(request, id):
    product_id = id
    quantity = request.POST['quantity']
    product = models.Product.objects.get(id=product_id)
    cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
    try:
        cart_product = models.CartProduct.objects.get(cart=cart, product=product)
        cart_product.quantity+=quantity
        cart_product.save()
    except:
        cart_product = models.CartProduct.objects.create(
            product=product, 
            cart=cart,
            quantity=quantity
        )
    return redirect('mycart')


def substractProductFromCart(request):
    code = request.GET['code']
    quantity = request.GET['quantity']
    product_cart = models.CartProduct.objects.get(generate_code=code)
    product_cart.quantity -= quantity
    product_cart.save()
    if not product_cart.quantity:
        product_cart.delete()
    return redirect('/')


def deleteProductCart(request):
    code = request.GET['code']
    product_cart = models.CartProduct.objects.get(generate_code=code)
    product_cart.delete()
    return redirect('/')


def CreateOrder(request):
    cart = models.Cart.objects.get(
        generate_code = request.GET['generate_code']
        )
    
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

    models.Order.objects.create(
        cart=cart,
        full_name = f"{request.user.first_name}, {request.user.last_name}",
        email = request.user.email,
        phone = request.GET['phone'],
        address = request.GET['address'],
        status = 1
        )
    cart.is_active = False
    cart.save()
    
    return redirect('/')