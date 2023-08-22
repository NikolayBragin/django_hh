# Generated by Django 4.2.4 on 2023-08-22 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_product_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product_count', models.IntegerField()),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.product')),
            ],
        ),
    ]