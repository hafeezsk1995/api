# Generated by Django 3.2.13 on 2022-04-29 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='company_name',
            new_name='title',
        ),
    ]
