# Generated by Django 3.1.4 on 2023-06-12 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0023_auto_20230612_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('c687212b-c321-4d74-9daf-b614be9d7155'), primary_key=True, serialize=False),
        ),
    ]
