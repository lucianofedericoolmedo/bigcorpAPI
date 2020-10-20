# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

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
    Department = apps.get_model("rest_api", "Department")
    db_alias = schema_editor.connection.alias

    with open('offices.json', encoding='utf-8') as file:
        offices = json.load(file)
        for office in offices:
            try:
                # Wrapping this line around...
                with transaction.atomic():
                    Office.objects.using(db_alias).get_or_create(
                        city=office["city"],
                        country=office["country"],
                        address=office["address"])
            except IntegrityError:
                continue
    with open('departments.json', encoding='utf-8') as file:
        departments = json.load(file)
        for department in departments:
            try:
                # Wrapping this line around...
                with transaction.atomic():
                    Department.objects.using(db_alias).get_or_create(
                        id=department['id'],
                        name=department["name"],
                        super_department= Department.objects.get(id=department["superdepartment"]) \
                        if isinstance(department["superdepartment"], int) else None)

            except IntegrityError as e:
                continue


def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass


class Migration(migrations.Migration):
    dependencies = [('rest_api', '0005_auto_20201020_1517')]
    operations = [
        migrations.RunPython(migrate_permissions, reverse_func),
        migrations.RunPython(forwards_func, reverse_func),
    ]
