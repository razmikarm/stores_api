# Generated by Django 5.0 on 2023-12-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='capacity',
            field=models.IntegerField(default=200, verbose_name='capacity'),
        ),
    ]
