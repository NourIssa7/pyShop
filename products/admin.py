from django.contrib import admin
from .models import Product, Offer
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')


admin.site.register(Product,ProductAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','Description')


admin.site.register(Offer,OfferAdmin)