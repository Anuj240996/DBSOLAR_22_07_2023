from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import Group

admin.site.site_header = 'DBSolar Dashboard'

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'quantity')
#     list_filter = ['category']
# Register your models here.c
#admin.site.register(Product, ProductAdmin)
#admin.site.unregister(Group)
admin.site.register(Customer)
