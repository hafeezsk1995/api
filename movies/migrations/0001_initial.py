# Generated by Django 3.2.13 on 2022-04-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=70)),
                ('released_year', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=20)),
                ('generes', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'movies',
                'managed': True,
            },
        ),
    ]
