# Generated by Django 5.0 on 2023-12-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_product_stores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stores',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='products', to='stores.store'),
        ),
    ]
