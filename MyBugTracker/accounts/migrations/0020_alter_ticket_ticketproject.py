# Generated by Django 4.1.5 on 2023-02-17 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_devuser_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='TicketProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tproject', to='accounts.project'),
        ),
    ]
