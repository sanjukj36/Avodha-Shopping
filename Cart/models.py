from django.db import models

# Create your models here.
from Shop.models import product


class cartlist(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    data_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class items(models.Model):
    prodt = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quan = models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.prodt)

    def total(self):
        return self.prodt.price*self.quan