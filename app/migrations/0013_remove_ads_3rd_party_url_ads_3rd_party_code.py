# Generated by Django 4.2.3 on 2023-11-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_useractivity_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads_3rd_party',
            name='url',
        ),
        migrations.AddField(
            model_name='ads_3rd_party',
            name='code',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]