# Generated by Django 3.2.6 on 2021-11-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectr_app', '0003_newcollectionrequest_new_collection_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='new_collection_name',
            field=models.CharField(max_length=500),
        ),
    ]
