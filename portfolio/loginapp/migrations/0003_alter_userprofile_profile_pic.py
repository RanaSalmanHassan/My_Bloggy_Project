# Generated by Django 4.1.1 on 2022-12-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pic', verbose_name='Profile Pic: '),
        ),
    ]
