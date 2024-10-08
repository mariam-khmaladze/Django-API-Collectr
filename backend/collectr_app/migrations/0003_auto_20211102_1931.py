# Generated by Django 3.2.6 on 2021-11-02 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectr_app', '0002_collection_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcollectionrequest',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='newcollectionrequest',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='newcollectionrequest',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
