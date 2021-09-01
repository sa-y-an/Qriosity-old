# Generated by Django 3.0.7 on 2020-07-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, default='hello')),
                ('background', models.FileField(upload_to='AudioQuestions/music')),
                ('image', models.ImageField(blank=True, upload_to='StaticQuestions/images')),
                ('image_url', models.URLField(blank=True)),
                ('files', models.FileField(upload_to='AudioQuestions/music')),
                ('hint', models.TextField(blank=True, default='hint')),
                ('answer', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]
