# Generated by Django 3.0.2 on 2020-03-20 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='img',
        ),
    ]