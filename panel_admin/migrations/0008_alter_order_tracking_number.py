# Generated by Django 4.2.6 on 2023-10-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_admin', '0007_alter_order_status_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA1c3767f2-d4bf-447e-ORDER', max_length=30, unique=True),
        ),
    ]
