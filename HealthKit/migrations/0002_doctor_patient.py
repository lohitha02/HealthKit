# Generated by Django 2.2.3 on 2019-07-06 08:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthKit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="'Name'")),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name="'Age'")),
                ('aadharNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999)], verbose_name="'Aadhar Number'")),
                ('email', models.EmailField(max_length=60, verbose_name="'Email Address'")),
                ('specialization', models.CharField(max_length=50, verbose_name="'Specialization'")),
                ('phoneNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name="'Phone Number'")),
                ('degree', models.TextField()),
                ('languages', models.ManyToManyField(to='HealthKit.Language')),
            ],
            options={
                'verbose_name_plural': "Doctor's",
                'verbose_name': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="'Name'")),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name="'Age'")),
                ('aadharNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999)], verbose_name="'Aadhar Number'")),
                ('email', models.EmailField(max_length=60, verbose_name="'Email Address'")),
                ('phoneNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name="'Phone Number'")),
                ('languages', models.ManyToManyField(to='HealthKit.Language')),
                ('previousDoctors', models.ManyToManyField(to='HealthKit.Doctor')),
            ],
            options={
                'verbose_name_plural': "Patient's",
                'verbose_name': 'Patient',
            },
        ),
    ]
