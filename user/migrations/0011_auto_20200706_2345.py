# Generated by Django 3.0.7 on 2020-07-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_solved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solved',
            old_name='player',
            new_name='gamer',
        ),
        migrations.AlterField(
            model_name='solved',
            name='level_on',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
