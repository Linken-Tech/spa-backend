# Generated by Django 4.2.10 on 2024-05-12 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_options_rename_is_staff_user_is_client_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="clientuser",
            table="client_user",
        ),
        migrations.AlterModelTable(
            name="masteruser",
            table="master_user",
        ),
    ]
