# Generated by Django 2.1.7 on 2019-05-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viyaan_app', '0004_auto_20190506_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='send_notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]