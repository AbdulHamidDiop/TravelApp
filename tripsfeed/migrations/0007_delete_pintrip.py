# Generated by Django 4.2.1 on 2023-06-03 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripsfeed', '0006_pintrip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PinTrip',
        ),
    ]