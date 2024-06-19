from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    code=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='img/')
    price=models.DecimalField(max_digits=2345,decimal_places=2)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name
class Client(models.Model):
    name=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.lastName

class Sale(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    date=models.DateField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.date