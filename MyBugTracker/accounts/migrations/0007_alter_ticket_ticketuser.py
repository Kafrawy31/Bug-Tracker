# Generated by Django 4.1.5 on 2023-01-31 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_devuser_project_devuser_userproject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='TicketUser',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.devuser'),
        ),
    ]
