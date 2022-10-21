# Generated by Django 4.1.2 on 2022-10-21 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0001_initial'),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='courier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courier.courier'),
            preserve_default=False,
        ),
    ]
