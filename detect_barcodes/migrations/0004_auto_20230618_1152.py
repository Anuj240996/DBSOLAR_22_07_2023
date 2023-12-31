# Generated by Django 3.1.4 on 2023-06-18 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detect_barcodes', '0003_barcodeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barcodeimage',
            name='old_image',
        ),
        migrations.AddField(
            model_name='barcodeimage',
            name='product_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='barcodeimage',
            name='AssignTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
