# Generated by Django 3.0.5 on 2020-04-19 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_remove_bid_contractor_pk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='to_client_mob',
        ),
    ]
