# Generated by Django 2.2.13 on 2020-10-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20201017_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
