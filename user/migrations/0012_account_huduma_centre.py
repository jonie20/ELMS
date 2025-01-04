# Generated by Django 5.1.3 on 2024-12-18 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_hudumacentre_remove_account_huduma_centre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='huduma_centre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='user.hudumacentre', verbose_name='Huduma Centre'),
        ),
    ]
