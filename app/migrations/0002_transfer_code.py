# Generated by Django 2.2.12 on 2020-05-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]