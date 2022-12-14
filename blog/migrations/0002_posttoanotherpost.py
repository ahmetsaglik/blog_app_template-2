# Generated by Django 4.0.4 on 2022-05-27 23:48

import blog.models
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostToAnotherPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('header_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=blog.models.get_header_image_filepath)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tag', models.CharField(max_length=50)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('post_to_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
                ('unlikes', models.ManyToManyField(blank=True, null=True, related_name='unlikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
