# Generated by Django 5.0 on 2023-12-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stores',
            field=models.ManyToManyField(blank=None, default=None, related_name='products', to='stores.store'),
        ),
    ]
