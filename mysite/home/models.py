from django.db import models

# Create your models here.

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