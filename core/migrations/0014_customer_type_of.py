# Generated by Django 4.0.1 on 2023-05-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type_of',
            field=models.CharField(default='SOME STRING', max_length=10),
        ),
    ]