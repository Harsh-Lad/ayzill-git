# Generated by Django 4.1.7 on 2023-02-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product_bottlevolume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.CharField(max_length=255),
        ),
    ]
