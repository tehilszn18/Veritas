# Generated by Django 4.1.7 on 2024-09-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_profile_profile_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pics',
            field=models.ImageField(default='', null=True, upload_to='pics'),
        ),
    ]
