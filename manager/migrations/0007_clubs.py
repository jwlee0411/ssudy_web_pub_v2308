# Generated by Django 4.0 on 2023-05-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_popup_content1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1_1', models.FileField(blank=True, null=True, upload_to='')),
                ('file1_2', models.FileField(blank=True, null=True, upload_to='')),
                ('file1_3', models.FileField(blank=True, null=True, upload_to='')),
                ('file2_1', models.FileField(blank=True, null=True, upload_to='')),
                ('file2_2', models.FileField(blank=True, null=True, upload_to='')),
                ('file2_3', models.FileField(blank=True, null=True, upload_to='')),
                ('file3_1', models.FileField(blank=True, null=True, upload_to='')),
                ('file3_2', models.FileField(blank=True, null=True, upload_to='')),
                ('file3_3', models.FileField(blank=True, null=True, upload_to='')),
                ('file4_1', models.FileField(blank=True, null=True, upload_to='')),
                ('calendar_check', models.BooleanField(default=False)),
            ],
        ),
    ]
