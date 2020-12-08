# Generated by Django 3.1.4 on 2020-12-06 16:40

import app.models.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Pets')),
                ('years', models.PositiveIntegerField(default=0, validators=[app.models.validators.max_value_years, app.models.validators.min_value])),
                ('months', models.PositiveIntegerField(default=0, validators=[app.models.validators.max_value_months, app.models.validators.min_value])),
                ('weeks', models.PositiveIntegerField(default=0, validators=[app.models.validators.max_value_weeks, app.models.validators.min_value])),
                ('type', models.CharField(choices=[('Dog', 'dog'), ('Cat', 'cat'), ('Bird', 'bird'), ('Reptile', 'reptile'), ('Other', 'other')], max_length=10)),
                ('description', models.TextField(default=' ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]