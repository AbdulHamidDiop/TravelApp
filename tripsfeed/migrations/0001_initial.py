# Generated by Django 4.2.1 on 2023-05-30 19:47

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('creationDate', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='postimages')),
                ('location', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField(blank=True)),
                ('partySize', models.SmallIntegerField(default=2)),
                ('description', models.TextField()),
            ],
        ),
    ]
