# Generated by Django 4.0 on 2021-12-15 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_image_comments_image_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default=None, upload_to='instagram')),
                ('bio', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='homepage.userprofile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='homepage.userprofile')),
            ],
        ),
    ]
