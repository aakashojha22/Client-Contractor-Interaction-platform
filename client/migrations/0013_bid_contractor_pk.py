# Generated by Django 3.0 on 2020-04-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20200406_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='contractor_pk',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
