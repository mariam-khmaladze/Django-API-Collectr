# Generated by Django 3.2.8 on 2021-11-07 07:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    replaces = [('collectr_app', '0002_collection_thumbnail'), ('collectr_app', '0003_auto_20211102_1931'), ('collectr_app', '0004_auto_20211104_0540'), ('collectr_app', '0005_auto_20211104_1409'), ('collectr_app', '0006_auto_20211106_1134'), ('collectr_app', '0007_auto_20211107_1812'), ('collectr_app', '0008_auto_20211107_1844')]

    dependencies = [
        ('collectr_app', '0001_initial'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='newcollectionrequest',
            name='cover_image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='cover_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='feedbackreviewrequest',
            name='evidence',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cover_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='evidence',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='newitemrequest',
            name='evidence',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='tradeattachment',
            name='attachment',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[512, 512], upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='cover_image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='collection',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='feedbackreviewrequest',
            name='evidence',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cover_image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='evidence',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='newitemrequest',
            name='evidence',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='tradeattachment',
            name='attachment',
            field=models.FileField(upload_to='attachments/'),
        ),
        migrations.AddConstraint(
            model_name='reputationfeedback',
            constraint=models.UniqueConstraint(fields=('receiver', 'sender'), name='rate-limiting-feedbacks'),
        ),
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
        migrations.RemoveField(
            model_name='newcollectionrequest',
            name='release_date',
        ),
        migrations.AddField(
            model_name='newitemrequest',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='newcollectionrequest',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='newitemrequest',
            name='add_to_collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collectr_app.collection'),
        ),
        migrations.DeleteModel(
            name='UserCollection',
        ),
    ]