# Generated by Django 2.0 on 2019-02-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0037_auto_20190206_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='Skill',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
