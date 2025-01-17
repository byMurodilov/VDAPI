# Generated by Django 5.0.6 on 2024-06-11 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veedeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=101, unique=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('vd_file', models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'wmv'])])),
                ('uploaded_tme', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
