# Generated by Django 3.2.10 on 2021-12-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20211224_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='push_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]