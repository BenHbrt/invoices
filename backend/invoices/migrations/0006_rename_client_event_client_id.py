# Generated by Django 4.2.7 on 2023-11-29 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_rename_client_id_event_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='client',
            new_name='client_id',
        ),
    ]
