# Generated by Django 3.2.5 on 2021-08-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
