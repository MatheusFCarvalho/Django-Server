# Generated by Django 4.2.2 on 2023-06-28 14:26

from django.db import migrations
import django.utils.timezone
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_billing',
            field=order.models.CustomDateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
