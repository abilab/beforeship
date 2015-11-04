# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('backer_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('order_date', models.CharField(max_length=256)),
                ('reward', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('financial_status', models.CharField(choices=[('CANC', 'Canceled'), ('PEND', 'Pending'), ('PARTLY_PAID', 'Partly Paid'), ('PAID', 'Paid')], max_length=256)),
                ('mail_receipt_status', models.BooleanField(default=False)),
                ('mail_receipt_path', models.FilePathField(path='.')),
                ('customer_data_confirmed', models.BooleanField(default=False)),
                ('billing_delivery_requested', models.BooleanField(default=False)),
                ('same_billing_and_shipping_address', models.BooleanField(default=True)),
                ('shipping_first_name', models.CharField(max_length=256)),
                ('shipping_last_name', models.CharField(max_length=256)),
                ('shipping_company', models.CharField(blank=True, max_length=256)),
                ('shipping_address_1', models.CharField(max_length=50)),
                ('shipping_address_2', models.CharField(null=True, blank=True, max_length=50)),
                ('shipping_city', models.CharField(max_length=256)),
                ('shipping_country', models.CharField(max_length=256)),
                ('shipping_state', models.CharField(blank=True, max_length=256)),
                ('shipping_postal_code', models.CharField(max_length=10)),
                ('shipping_phone', models.CharField(blank=True, max_length=20)),
                ('billing_first_name', models.CharField(max_length=256)),
                ('billing_last_name', models.CharField(max_length=256)),
                ('billing_company', models.CharField(blank=True, max_length=256)),
                ('billing_address_1', models.CharField(max_length=50)),
                ('billing_address_2', models.CharField(null=True, blank=True, max_length=50)),
                ('billing_city', models.CharField(max_length=256)),
                ('billing_country', models.CharField(max_length=256)),
                ('billing_state', models.CharField(blank=True, max_length=256)),
                ('billing_postal_code', models.CharField(max_length=10)),
                ('billing_phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
