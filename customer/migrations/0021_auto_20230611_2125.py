# Generated by Django 3.1.4 on 2023-06-11 15:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_auto_20230611_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('2e33933c-a3ed-428d-948e-c73922abc351'), primary_key=True, serialize=False),
        ),
    ]
