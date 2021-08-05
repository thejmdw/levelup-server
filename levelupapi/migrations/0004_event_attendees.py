# Generated by Django 3.2.5 on 2021-08-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_rename_name_game_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.EventGamer', to='levelupapi.Gamer'),
        ),
    ]