# Generated by Django 4.0.5 on 2022-08-23 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0013_dbs_nsap_dbs_other_delete_db_nsaps_delete_db_others'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='emp_mname',
        ),
    ]
