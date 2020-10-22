# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.models import User     # where User lives
import os                                      # env var access
from django.contrib.auth.management import create_permissions


def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def forwards_func(apps, schema_editor):
    # build the user you now have access to via Django magic
    if not User.objects.filter(username='admin').exists() : 
      user = User.objects.create_superuser('admin', password='superuser123', email='admin@admin.com')
      #ADMIN = 'ADM'
      #ProfileService.create_profile('admin','', user, ADMIN)
    else:
      print('Superuser already created')


def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass


class Migration(migrations.Migration):
    dependencies = [('rest_api', '0001_initial')]
    operations = [
        migrations.RunPython(migrate_permissions, reverse_func),
        migrations.RunPython(forwards_func, reverse_func),
    ]
