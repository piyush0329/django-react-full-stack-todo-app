# Generated by Django 5.1 on 2024-08-29 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_familydetails_total_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familydetails',
            name='brother_name',
        ),
        migrations.CreateModel(
            name='Brother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brothers', to='api.familydetails')),
            ],
        ),
        migrations.CreateModel(
            name='Sister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sisters', to='api.familydetails')),
            ],
        ),
    ]
