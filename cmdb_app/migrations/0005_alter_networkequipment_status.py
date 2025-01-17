# Generated by Django 4.2.17 on 2025-01-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cmdb_app", "0004_alter_networkequipment_ip_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networkequipment",
            name="status",
            field=models.CharField(
                choices=[("active", "Active"), ("inactive", "Inactive")],
                default="inactif",
                max_length=20,
            ),
        ),
    ]
