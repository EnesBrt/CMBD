# Generated by Django 4.2.17 on 2025-01-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cmdb_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="networkequipment",
            name="host",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="networkequipment",
            name="port",
            field=models.IntegerField(null=True),
        ),
    ]
