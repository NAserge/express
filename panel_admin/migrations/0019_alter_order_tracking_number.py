# Generated by Django 3.2.23 on 2023-11-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_admin', '0018_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWAae9d4d58-21bb-4ced-ORDER', max_length=30, unique=True),
        ),
    ]