# Generated by Django 4.1.5 on 2023-02-14 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_ticket_ticketsubmittedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='TicketAssignedTo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Ticket_assigned_to', to='accounts.devuser'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='TicketSubmittedBy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Ticket_submitted_by', to='accounts.devuser'),
        ),
    ]
