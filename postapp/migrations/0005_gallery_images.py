# Generated by Django 4.2.7 on 2023-11-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0004_alter_imagespost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gallery/images')),
            ],
            options={
                'ordering': ('-title',),
            },
        ),
    ]