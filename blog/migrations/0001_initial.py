# Generated by Django 4.1.3 on 2023-01-02 15:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('intro', models.CharField(max_length=255)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('imagen', models.ImageField(upload_to='media')),
                ('autor', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
            ],
        ),
    ]