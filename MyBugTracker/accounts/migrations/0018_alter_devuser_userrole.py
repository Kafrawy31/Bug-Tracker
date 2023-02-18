# Generated by Django 4.1.5 on 2023-02-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_rename_ticketassignedto_ticket_ticketassignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devuser',
            name='UserRole',
            field=models.TextField(choices=[('Developer', 'DEV'), ('SEN', 'Senior'), ('ADM', 'Admin')], max_length=12, null=True),
        ),
    ]
