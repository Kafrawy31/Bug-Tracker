# Generated by Django 4.1.5 on 2023-02-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_ticket_ticketuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='TicketPriority',
            field=models.CharField(choices=[('VH', 'Very Important'), ('H', 'Important'), ('Medium', 'Medium'), ('L', 'Low')], max_length=16),
        ),
    ]
