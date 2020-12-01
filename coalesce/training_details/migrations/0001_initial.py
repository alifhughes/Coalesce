# Generated by Django 3.0.8 on 2020-11-27 16:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(help_text='Name of the training')),
                ('link', models.URLField(help_text='Link to online training course')),
                ('date', models.DateField(help_text='Date of the training')),
            ],
        ),
    ]
