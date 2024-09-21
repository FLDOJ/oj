# Generated by Django 2.2.10 on 2020-03-30 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0101_submission_judged_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='api_token',
            field=models.CharField(help_text='64 character hex-encoded API access token', max_length=64, null=True, validators=[django.core.validators.RegexValidator('^[a-f0-9]{64}$', 'API token must be None or hexadecimal')], verbose_name='API token'),
        ),
    ]
