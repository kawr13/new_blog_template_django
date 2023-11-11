# Generated by Django 4.2.7 on 2023-11-11 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postapp.post')),
            ],
        ),
    ]