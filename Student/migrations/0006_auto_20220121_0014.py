# Generated by Django 3.2.9 on 2022-01-20 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_alter_studentprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='username',
        ),
    ]