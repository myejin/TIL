# Generated by Django 3.2.8 on 2021-10-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='actors', to='movies.Movie'),
        ),
    ]
