# Generated by Django 3.2.6 on 2021-11-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectr_app', '0003_auto_20211102_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackreviewrequest',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newcollectionrequest',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newitemrequest',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='cover_image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]