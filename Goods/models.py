from django.db import models
from django.contrib.auth.models import User
from random import sample
import string

class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/')
    img = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    img = models.ImageField()
    generate_code = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name:str = models.CharField(max_length=255)
    quantity:int = models.PositiveIntegerField(default=1)
    price:float = models.DecimalField(max_digits=8, decimal_places=2)
    category:Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description:str = models.TextField()

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product-img')

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    shopping_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.author.username


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    status = models.SmallIntegerField(
        choices=(
            (1, 'Tayyorlanmoqda'),
            (2, 'Yo`lda'),
            (3, 'Yetib borgan'),
            (4, 'Qabul qilingan'),
            (5, 'Qaytarilgan'),
        )
    )

    def __str__(self):
        return self.full_name
