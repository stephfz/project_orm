# Generated by Django 2.2.4 on 2021-05-03 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0011_remove_director_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='app_orm.Genre'),
            preserve_default=False,
        ),
    ]
