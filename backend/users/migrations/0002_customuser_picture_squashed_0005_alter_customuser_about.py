# Generated by Django 3.2.8 on 2021-11-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('users', '0002_customuser_picture'), ('users', '0003_alter_customuser_picture'), ('users', '0004_alter_customuser_picture'), ('users', '0005_alter_customuser_about')]

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(default="A bio hasn't been added yet.", max_length=500, verbose_name='about'),
        ),
    ]