# Generated by Django 4.0.5 on 2022-08-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0016_rename_pl_family_id_otherdata_bpl_family_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsapdata',
            name='faulty',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
