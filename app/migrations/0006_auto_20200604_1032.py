# Generated by Django 2.2.12 on 2020-06-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200525_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_eight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_eleven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_five',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_four',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_nine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_seven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_six',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_ten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_twelve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True, verbose_name='Charges')),
            ],
        ),
        migrations.RenameField(
            model_name='transfer',
            old_name='code',
            new_name='sending_branch_code',
        ),
        migrations.AlterField(
            model_name='transfer',
            name='charges',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
