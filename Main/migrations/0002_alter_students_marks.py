# Generated by Django 4.0.4 on 2022-08-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='marks',
            field=models.IntegerField(),
        ),
    ]
