from django.contrib import admin

# Register your models here.
from .models import *



class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(categ,catagdmin)



class prodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug','price','stock','img','category','avilable']
    list_editable = ['price','stock','img','avilable']
admin.site.register(product,prodAdmin)