# Generated by Django 4.2.4 on 2023-09-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aemail', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=25)),
            ],
        ),
    ]
