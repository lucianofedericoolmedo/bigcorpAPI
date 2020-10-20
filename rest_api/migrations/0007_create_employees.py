# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import requests
from django.db import migrations, transaction, IntegrityError
from django.contrib.auth.models import User  # where User lives
import os  # env var access
from django.contrib.auth.management import create_permissions


def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def forwards_func(apps, schema_editor):
    # build the user you now have access to via Django magic
    load_data(apps, schema_editor)


def load_data(apps, schema_editor):
    Office = apps.get_model("rest_api", "Office")
    Employee = apps.get_model("rest_api", "Employee")
    Department = apps.get_model("rest_api", "Department")
    db_alias = schema_editor.connection.alias

    url = 'https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees'
    response = requests.get(url)
    data = response.json()
    for item in data:
        with transaction.atomic():
            elem, _ = Employee.objects.using(db_alias).get_or_create(
                id=item['id'])
            elem, _ = Employee.objects.get_or_create(id=item['id'])
            elem.first = item['first']
            elem.last = item['last']
            elem.manager = Employee.objects.get(id=item['manager']) if item['manager'] is not None else None
            elem.department = Department.objects.get(id=item['department']) if item['department'] is not None else None
            elem.office = Office.objects.get(id=item['office']) if item['office'] is not None else None
            elem.save()


def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass


class Migration(migrations.Migration):
    dependencies = [('rest_api', '0006_create_offices_and_departments')]
    operations = [
        migrations.RunPython(migrate_permissions, reverse_func),
        migrations.RunPython(forwards_func, reverse_func),
    ]
