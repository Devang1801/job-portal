# Generated by Django 3.2.16 on 2023-04-23 14:38

from django.db import migrations, models
import jobapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_auto_20230423_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='cover_letter',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='applicant',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='applicant',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='applicant',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='applicant',
            name='resume',
            field=models.URLField(default=None),
        ),
    ]
