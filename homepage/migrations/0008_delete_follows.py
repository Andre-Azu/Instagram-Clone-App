# Generated by Django 4.0 on 2021-12-15 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_userprofile_follows'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follows',
        ),
    ]