from django.db import models
from users.models import User
# Create your models here.

class ProductCategory(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    def __str__(self):
        return f"Product:{self.name}, description: {self.description}\nCategory: {self.category.name}"
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum()for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()



    def __str__(self):
        return f'Cart for {self.user.username} | Product: {self.product.name}'

    def sum(self):
        return self.product.price*self.quantity












