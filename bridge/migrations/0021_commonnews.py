# Generated by Django 2.0 on 2019-01-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0020_auto_20190120_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(null=True)),
            ],
        ),
    ]