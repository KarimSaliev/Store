from django.contrib import admin

# Register your models here.
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name','description','price','quantity','image','category')
    search_fields = ('name',)
    ordering = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'create_timestamp')
    readonly_fields = ('create_timestamp',)
    extra = 0