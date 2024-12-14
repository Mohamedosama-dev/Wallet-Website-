# Generated by Django 5.1.1 on 2024-09-14 12:50

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_transaction_wallet_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_credit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
