# Generated by Django 3.1.3 on 2021-05-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fileupload',
            fields=[
                ('fileupload', models.FileField(upload_to='')),
                ('file_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]