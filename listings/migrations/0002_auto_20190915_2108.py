# Generated by Django 2.2.5 on 2019-09-15 11:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
