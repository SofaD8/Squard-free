# Generated by Django 5.0.6 on 2024-05-21 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_team_options_photo_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['sort'], 'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
    ]
