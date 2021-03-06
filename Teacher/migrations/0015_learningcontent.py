# Generated by Django 3.2.9 on 2022-01-25 19:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0014_auto_20220125_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningContent',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='LearningContentImages/')),
                ('video', models.FileField(blank=True, null=True, upload_to='LearningContentVideos/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
