# Generated by Django 4.2.5 on 2023-09-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('et_app', '0003_entry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
