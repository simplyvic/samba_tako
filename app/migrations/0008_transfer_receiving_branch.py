# Generated by Django 2.2.12 on 2020-06-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200604_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='receiving_branch',
            field=models.CharField(blank=True, choices=[('001 BAKAU', '001 BAKAU'), ('002 BRUSUBI', '002 BRUSUBI'), ('003 BRUFUT', '003 BRUFUT'), ('004 TALLINDING', '004 TALLINDING'), ('005 TIPPER GARRAGE', '005 TIPPER GARRAGE'), ('006 BANSANG 1', '006 BANSANG 1'), ('007 JANGJANGBUREH', '007 JANGJANGBUREH'), ('008 BRIKAMA BA', '008 BRIKAMA BA'), ('009 BANSANG 2', '009 BANSANG 2'), ('010 SOMA', '010 SOMA'), ('011 BASSE', '011 BASSE'), ('012 SINCHU', '012 SINCHU')], max_length=30, null=True),
        ),
    ]