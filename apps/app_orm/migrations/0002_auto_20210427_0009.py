# Generated by Django 2.2.4 on 2021-04-27 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='duration',
            new_name='duration_in_mins',
        ),
    ]