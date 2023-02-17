from django.contrib import admin

# Register your models here.
from .models import cartlist,items

admin.site.register(cartlist)
admin.site.register(items)