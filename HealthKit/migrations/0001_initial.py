# Generated by Django 2.2.3 on 2019-07-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name="'Language Name'")),
            ],
        ),
    ]
