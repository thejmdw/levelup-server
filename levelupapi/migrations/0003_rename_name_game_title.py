# Generated by Django 3.2.5 on 2021-08-03 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_game_skill_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
    ]