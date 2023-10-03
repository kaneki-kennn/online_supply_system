from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Requester (models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self)   :
        return self.name
    
class Tag (models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self)   :
        return self.name

class Products(models.Model):

    CATEGORY = (
    ('Sports', 'Sports'),
    ('Laboratory', 'Laboratory')
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    description = models.CharField(max_length=200,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self)   :
        return self.name


class Status(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )

    requester = models.ForeignKey(Requester, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)      
    status = models.CharField(max_length=200,null=True, choices=STATUS)



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


def __str__(self):
        return self.message
    

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_unit = models.CharField(max_length=50)
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models



# Create your models here.

class Requester (models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self)   :
        return self.name
    
class Tag (models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self)   :
        return self.name


from django.db import models
class Products(models.Model):

    CATEGORY = (
    ('Sports', 'Sports'),
    ('Laboratory', 'Laboratory')
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    description = models.CharField(max_length=200,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self)   :
        return self.name


class Status(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )

    requester = models.ForeignKey(Requester, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)      
    status = models.CharField(max_length=200,null=True, choices=STATUS)


from django.db import models

class Item(models.Model):
    item_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    unit = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
