# Generated by Django 4.1.1 on 2022-09-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_products_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='affiliate_link',
            field=models.CharField(blank=True, max_length=2083, null=True, verbose_name='bussines_link'),
        ),
    ]