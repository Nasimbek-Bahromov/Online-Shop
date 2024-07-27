from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist
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
    img = models.ImageField(upload_to='category_img')

    def __str__(self):
        return self.name



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



class ProductEnter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    old_quantity = models.IntegerField(blank=True, null=True)  # Allow null for new instances
    date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not self.id:
                self.old_quantity = self.product.quantity
                self.product.quantity += int(self.quantity)
            else:
                try:
                    previous_entry = ProductEnter.objects.get(id=self.id)
                    quantity_diff = int(self.quantity) - previous_entry.quantity
                    self.product.quantity += quantity_diff
                    self.old_quantity = previous_entry.quantity
                except ObjectDoesNotExist:
                    # Handle case where the entry doesn't exist
                    pass
            self.product.save()
            super().save(*args, **kwargs)
