# Generated by Django 3.1.4 on 2023-06-16 15:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0039_auto_20230616_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('a5eaecdd-0405-4aec-9b76-4621ee974736'), primary_key=True, serialize=False),
        ),
    ]