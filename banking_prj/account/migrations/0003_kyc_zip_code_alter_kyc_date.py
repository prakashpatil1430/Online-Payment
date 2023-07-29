# Generated by Django 4.2.3 on 2023-07-29 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_account_ref_code_kyc"),
    ]

    operations = [
        migrations.AddField(
            model_name="kyc",
            name="zip_code",
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="kyc",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
