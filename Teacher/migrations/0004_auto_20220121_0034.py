# Generated by Django 3.2.9 on 2022-01-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0003_auto_20220121_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]