# Generated by Django 4.0.5 on 2022-07-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triangle', '0002_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='form',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]