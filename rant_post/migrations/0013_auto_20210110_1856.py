# Generated by Django 3.1.3 on 2021-01-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rant_post', '0012_auto_20210110_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rantpost',
            name='text',
            field=models.TextField(max_length=2000),
        ),
    ]