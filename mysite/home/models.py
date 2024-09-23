from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharastra', 'Maharastra'),
)

CATEGORY_CHOICES = (
    ('BS', 'Barik Sev'),
    ('MS', 'Moti Sev'),
    ('CD', 'Chana Dal'),
    ('CB', 'Chatpati Boondi'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    sp = models.FloatField()
    dp = models.FloatField()
    desc = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.PositiveIntegerField(default=0)
    zipcode = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name