# Generated by Django 3.2.8 on 2021-11-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectr_app', '0006_auto_20211106_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcollectionrequest',
            name='new_collection_name',
        ),
        migrations.RemoveField(
            model_name='newitemrequest',
            name='new_item_name',
        ),
        migrations.AddField(
            model_name='feedbackreviewrequest',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='feedbackreviewrequest',
            name='new_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='newcollectionrequest',
            name='new_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='newitemrequest',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='newitemrequest',
            name='new_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='collection',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='feedbackreviewrequest',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='feedbackreviewrequest',
            name='evidence',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='item',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='evidence',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='newitemrequest',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='newitemrequest',
            name='evidence',
            field=models.TextField(max_length=5000),
        ),
    ]