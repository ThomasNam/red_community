# Generated by Django 3.0.7 on 2020-06-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardtag', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='boardtag.BoardTag', verbose_name='태그'),
        ),
    ]
