# Generated by Django 3.0 on 2020-04-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contractor', '0006_contractorlogin_sample_work_6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorlogin',
            name='sample_work_6',
            field=models.ImageField(blank=True, upload_to='sample_work_6'),
        ),
    ]