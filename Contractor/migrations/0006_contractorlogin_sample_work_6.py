# Generated by Django 3.0 on 2020-03-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contractor', '0005_auto_20200327_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorlogin',
            name='sample_work_6',
            field=models.ImageField(blank=True, upload_to='sample_work_5'),
        ),
    ]
