# Generated by Django 2.2.4 on 2021-05-04 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0013_auto_20210504_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]