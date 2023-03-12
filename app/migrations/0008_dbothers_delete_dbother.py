# Generated by Django 4.0.5 on 2022-08-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0007_nopension_delete_no_pension'),
    ]

    operations = [
        migrations.CreateModel(
            name='dbothers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='dbother',
        ),
    ]