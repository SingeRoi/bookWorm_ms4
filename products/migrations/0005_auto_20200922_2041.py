# Generated by Django 3.1.1 on 2020-09-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200921_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
