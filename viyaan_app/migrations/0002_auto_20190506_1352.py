# Generated by Django 2.1.7 on 2019-05-06 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viyaan_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='is_staff',
            new_name='community',
        ),
    ]