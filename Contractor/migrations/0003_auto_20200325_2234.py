# Generated by Django 3.0 on 2020-03-25 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contractor', '0002_auto_20200323_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contractorlogin',
            old_name='User',
            new_name='user',
        ),
    ]
