# Generated by Django 2.0 on 2019-01-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0008_auto_20190112_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='Icard_Picture',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='Personal_Email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expert',
            name='Profile_piture',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]
