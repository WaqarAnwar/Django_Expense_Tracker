# Generated by Django 4.2.5 on 2023-09-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('et_app', '0002_rename_created_at_entry_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='options',
            field=models.CharField(choices=[('cash_in', 'Cash In'), ('cash_out', 'Cash Out')], max_length=20, null=True),
        ),
    ]
