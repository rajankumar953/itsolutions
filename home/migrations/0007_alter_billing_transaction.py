# Generated by Django 4.2 on 2023-05-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_billing_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='transaction',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
