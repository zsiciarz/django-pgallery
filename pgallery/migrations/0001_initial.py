# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields
import model_utils.fields
import django.contrib.postgres.fields
import django.utils.timezone
from django.conf import settings
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='slug')),
                ('description', markitup.fields.MarkupField(no_rendered_field=True, verbose_name='description')),
                ('shot_date', models.DateField(null=True, verbose_name='shot date', blank=True)),
                ('_description_rendered', models.TextField(editable=False, blank=True)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='author', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['-shot_date'],
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='image')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('exif', django.contrib.postgres.fields.hstore.HStoreField(default={}, editable=False, db_index=True)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='author', on_delete=models.CASCADE)),
                ('gallery', models.ForeignKey(related_name='photos', verbose_name='gallery', to='pgallery.Gallery', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name_plural': 'Photos',
            },
        ),
    ]
