from .models import Product, Offer
from django.contrib import admin


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)

admin.site.register(Offer, OfferAdmin)
