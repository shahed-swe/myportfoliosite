# Generated by Django 2.2 on 2019-10-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
