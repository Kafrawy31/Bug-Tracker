# Generated by Django 4.1.5 on 2023-02-14 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_ticket_ticketsubmittedby_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='TicketSubmittedBy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Ticket_submitted_by', to='accounts.devuser'),
        ),
    ]
