# Generated by Django 3.2.9 on 2022-01-23 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0012_classroom_homework'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='homework',
        ),
        migrations.AddField(
            model_name='homeworkteachercanadd',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.classroom'),
        ),
    ]