# Generated by Django 4.0 on 2023-06-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_remove_maintenance_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(blank=True, null=True, upload_to='')),
                ('file2', models.FileField(blank=True, null=True, upload_to='')),
                ('file3', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
