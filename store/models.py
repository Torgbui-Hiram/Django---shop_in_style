from django.db import models


class Product(models.Model):
    name = models.CharField('product_name', max_length=200)
    price = models.CharField('product_price', max_length=50)
    image_url = models.CharField('product_image', max_length=2083)
    info = models.TextField('product_info')
    date = models.DateTimeField('date_added')
    affiliate_link = models.CharField(
        'bussines_link', max_length=2083, blank=True, null=True)
    manager = models.CharField('Owner', max_length=50, default='admin')
    advert = models.TextField('Amazon')
