# Generated by Django 4.1.5 on 2023-04-23 05:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('e969c58e-2fc3-408e-b8d6-6a0533678520'), primary_key=True, serialize=False),
        ),
    ]