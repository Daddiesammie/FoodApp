# Generated by Django 4.2.7 on 2024-07-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sitesettings_site_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettings',
            old_name='Site_description',
            new_name='site_description',
        ),
    ]
