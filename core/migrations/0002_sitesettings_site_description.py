# Generated by Django 4.2.7 on 2024-07-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='Site_description',
            field=models.TextField(default='Welcome to my site'),
        ),
    ]