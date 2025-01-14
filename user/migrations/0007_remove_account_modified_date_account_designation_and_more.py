# Generated by Django 5.1.3 on 2024-12-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_account_modified_date_account_total_leave_days_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='account',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='id_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='account',
            name='personal_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
