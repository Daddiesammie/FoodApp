# Generated by Django 4.2.7 on 2024-07-04 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitem_image'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'menu_item')},
        ),
    ]
