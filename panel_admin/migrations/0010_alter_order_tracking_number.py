# Generated by Django 4.2.6 on 2023-10-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_admin', '0009_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA970b41ee-aea4-4d40-ORDER', max_length=30, unique=True),
        ),
    ]
