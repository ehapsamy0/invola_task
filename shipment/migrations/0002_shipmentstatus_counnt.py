# Generated by Django 4.1.2 on 2022-10-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentstatus',
            name='counnt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
