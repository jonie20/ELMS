# Generated by Django 5.1.3 on 2024-12-12 07:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_account_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='huduma_centre',
            field=models.CharField(blank=True, max_length=100, verbose_name='Huduma Centre'),
        ),
        migrations.AddField(
            model_name='account',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_employees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='carry_forward_days',
            field=models.IntegerField(default=0, verbose_name='Carry Forward Days'),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='no_of_days',
            field=models.IntegerField(default=15, verbose_name='Number of Days'),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='total_leave_days',
            field=models.IntegerField(default=15, verbose_name='Total Leave Days'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='admin_remark_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='admin_remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='leave_type',
            field=models.CharField(choices=[('SL', 'Sick Leave'), ('CL', 'Casual Leave'), ('EL', 'Emergency Leave')], max_length=2),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='posting_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='to_date',
            field=models.DateField(),
        ),
    ]