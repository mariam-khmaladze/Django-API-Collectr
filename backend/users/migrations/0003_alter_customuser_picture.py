# Generated by Django 3.2 on 2021-11-04 14:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='uploads/'),
        ),
    ]