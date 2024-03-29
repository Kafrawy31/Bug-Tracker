# Generated by Django 4.1.5 on 2023-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_ticket_ticketassignedto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='TicketSubmittedBy',
        ),
        migrations.AlterField(
            model_name='devuser',
            name='UserRole',
            field=models.TextField(choices=[('DEV', 'Developer'), ('SEN', 'Senior'), ('ADM', 'Admin')], max_length=12, null=True),
        ),
    ]
