# Generated by Django 4.1.1 on 2022-09-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_affiliate_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manager',
            field=models.CharField(default=1, max_length=50, verbose_name='Owner'),
        ),
    ]
