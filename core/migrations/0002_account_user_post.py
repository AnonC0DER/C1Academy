# Generated by Django 3.2.9 on 2022-01-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_post',
            field=models.CharField(blank=True, choices=[('superuser', 'Superuser'), ('manager', 'Manager'), ('teacher', 'Teacher'), ('student', 'Student')], max_length=75, null=True),
        ),
    ]
