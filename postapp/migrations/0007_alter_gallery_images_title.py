# Generated by Django 4.2.7 on 2023-11-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0006_alter_gallery_images_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery_images',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]