# Generated by Django 3.2.9 on 2022-01-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0006_alter_classroom_home_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='home_work',
            field=models.ManyToManyField(default=None, to='Teacher.HomeworkTeacherCanAdd'),
        ),
    ]
