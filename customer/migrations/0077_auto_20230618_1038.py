# Generated by Django 3.1.4 on 2023-06-18 05:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0076_auto_20230618_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('b5b31780-fa2f-4cff-a2a5-1d66acbc74c6'), primary_key=True, serialize=False),
        ),
    ]
