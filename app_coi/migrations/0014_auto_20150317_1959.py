# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coi', '0013_auto_20150317_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='img',
            field=models.ImageField(upload_to=b'staticfiles/media/people'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(upload_to=b'staticfiles/media/people'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitingscholar',
            name='img',
            field=models.ImageField(upload_to=b'staticfiles/media/people'),
            preserve_default=True,
        ),
    ]
