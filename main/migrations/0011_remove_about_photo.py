# Generated by Django 5.0.6 on 2024-06-14 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_about_photo_alter_about_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='photo',
        ),
    ]
