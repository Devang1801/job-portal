# Generated by Django 3.2.16 on 2023-04-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0018_auto_20230423_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
