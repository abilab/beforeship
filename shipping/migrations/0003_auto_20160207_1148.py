# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20151114_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='shop_source',
        ),
        migrations.DeleteModel(
            name='ShopSources',
        ),
    ]
