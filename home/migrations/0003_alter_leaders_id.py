# Generated by Django 3.2.7 on 2021-09-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200830_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaders',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
