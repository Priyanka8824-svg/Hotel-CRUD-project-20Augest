# Generated by Django 5.1 on 2024-08-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hid', models.IntegerField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
