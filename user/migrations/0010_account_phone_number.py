# Generated by Django 5.1.3 on 2024-12-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_account_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
