# Generated by Django 3.2.15 on 2023-01-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_front'),
    ]

    operations = [
        migrations.AddField(
            model_name='front',
            name='content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='front',
            name='content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='front',
            name='content3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='front',
            name='title1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='front',
            name='title2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='front',
            name='title3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
