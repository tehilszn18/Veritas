# Generated by Django 4.1.7 on 2024-09-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
