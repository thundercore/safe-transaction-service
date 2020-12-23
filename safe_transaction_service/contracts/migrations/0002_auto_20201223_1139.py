# Generated by Django 3.1.4 on 2020-12-23 11:39

from django.db import migrations, models
import safe_transaction_service.contracts.models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractabi',
            name='abi',
            field=models.JSONField(unique=True, validators=[safe_transaction_service.contracts.models.validate_abi]),
        ),
    ]