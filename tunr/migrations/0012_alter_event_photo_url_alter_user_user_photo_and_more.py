# Generated by Django 5.0.7 on 2024-07-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0011_alter_event_photo_url_alter_user_user_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='photo_url',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
    ]
