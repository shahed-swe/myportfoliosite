# Generated by Django 2.2.4 on 2019-10-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20191011_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
