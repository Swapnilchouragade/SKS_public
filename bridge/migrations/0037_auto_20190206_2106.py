# Generated by Django 2.0 on 2019-02-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0036_auto_20190206_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Personal_Email',
            field=models.EmailField(max_length=100),
        ),
    ]