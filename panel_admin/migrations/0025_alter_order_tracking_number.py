# Generated by Django 3.2.23 on 2024-05-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_admin', '0024_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA90fd8102-4c41-43af-ORDER', max_length=30, unique=True),
        ),
    ]
