# Generated by Django 4.2.1 on 2023-05-28 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_traveller_preferences_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravellerPreferences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('distance', models.CharField(blank=True, default='0', max_length=1)),
                ('interests', models.CharField(blank=True, default='0', max_length=1)),
                ('partySize', models.SmallIntegerField(blank=True, default='0')),
            ],
        ),
        migrations.AddField(
            model_name='traveller',
            name='preferences',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.travellerpreferences'),
            preserve_default=False,
        ),
    ]