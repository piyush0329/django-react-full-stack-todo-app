# Generated by Django 5.1 on 2024-08-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_familydetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familydetails',
            name='total_members',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
