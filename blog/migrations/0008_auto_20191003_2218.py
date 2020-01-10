# Generated by Django 2.2 on 2019-10-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.SlugField(),
        ),
    ]
