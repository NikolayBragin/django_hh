# Generated by Django 4.2.4 on 2023-08-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_product_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_city',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_amount',
            field=models.IntegerField(),
        ),
    ]
