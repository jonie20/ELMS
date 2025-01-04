# Generated by Django 5.1.3 on 2024-12-15 13:08

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_account_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=user.models.generate_unique_name),
        ),
    ]
