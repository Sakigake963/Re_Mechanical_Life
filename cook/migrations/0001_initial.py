# Generated by Django 4.2.2 on 2023-06-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('info_food', models.TextField()),
                ('condition_food', models.TextField()),
            ],
        ),
    ]