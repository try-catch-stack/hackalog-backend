# Generated by Django 3.1.4 on 2021-02-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210126_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
