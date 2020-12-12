# Generated by Django 3.1.4 on 2020-12-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='location',
            field=models.TextField(default='Sofia', max_length=20),
        ),
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]