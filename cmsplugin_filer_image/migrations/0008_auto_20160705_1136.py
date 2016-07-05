# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0007_filerimage_link_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_filer_image_filerimage', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, help_text='Optional. Adds HTML attributes to the rendered link.'),
        ),
    ]