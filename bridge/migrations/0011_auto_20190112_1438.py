# Generated by Django 2.0 on 2019-01-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0010_auto_20190112_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='Icard_Picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='Profile_piture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
