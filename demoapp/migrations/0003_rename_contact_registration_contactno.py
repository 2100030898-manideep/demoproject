# Generated by Django 4.2.5 on 2023-09-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='contact',
            new_name='contactno',
        ),
    ]
