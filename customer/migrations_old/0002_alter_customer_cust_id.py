# Generated by Django 4.1.5 on 2023-04-23 05:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('f6235a5f-a87b-45e1-93dd-8bb0254e3c96'), primary_key=True, serialize=False),
        ),
    ]
