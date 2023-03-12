# Generated by Django 4.0.5 on 2022-08-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0010_dbnsaps_delete_dbnsap'),
    ]

    operations = [
        migrations.CreateModel(
            name='db_nsaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('pension_id', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('income', models.CharField(max_length=20)),
                ('disability', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='db_others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('disability', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_fname', models.CharField(max_length=30)),
                ('emp_lname', models.CharField(max_length=30)),
                ('emp_mname', models.CharField(max_length=30)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='dbnsaps',
        ),
        migrations.DeleteModel(
            name='dbothers',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
