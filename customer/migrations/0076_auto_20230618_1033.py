# Generated by Django 3.1.4 on 2023-06-18 05:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0075_auto_20230618_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('ef9a65b0-8626-44cb-b461-31e6f039a6cb'), primary_key=True, serialize=False),
        ),
    ]
