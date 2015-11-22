# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('shop_name', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=256)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'shops',
                'verbose_name': 'shop',
            },
        ),
        migrations.CreateModel(
            name='ShopSources',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('source', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'shop sources',
                'verbose_name': 'shop source',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'orders', 'verbose_name': 'order'},
        ),
        migrations.AddField(
            model_name='shops',
            name='shop_source',
            field=models.ForeignKey(to='shipping.ShopSources'),
        ),
        migrations.AddField(
            model_name='order',
            name='shop_id',
            field=models.ForeignKey(to='shipping.Shops', default=1),
            preserve_default=False,
        ),
    ]
