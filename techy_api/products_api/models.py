from django.db import models
from user_auth.models import UserAccount

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    itemType = models.CharField(max_length=250)
    useraccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)