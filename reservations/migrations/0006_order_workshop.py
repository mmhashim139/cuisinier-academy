# Generated by Django 3.1.5 on 2021-01-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_workshop_expert'),
        ('reservations', '0005_auto_20210125_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='workshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshops.workshop'),
        ),
    ]
