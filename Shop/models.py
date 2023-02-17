from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('Prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)



class product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    img = models.ImageField(upload_to='product')
    dec = models.TextField()
    stock = models.IntegerField()
    avilable = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
