# Generated by Django 4.2.7 on 2024-07-04 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_extra_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_reference',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
