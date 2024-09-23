# Generated by Django 5.1 on 2024-08-10 11:14

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('content', models.TextField()),
                ('blog_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('0', 'DRAFT'), ('1', 'PUBLISH')], default='0', max_length=1)),
                ('section', models.CharField(choices=[('Recent', 'Recent'), ('Publish', 'Publish'), ('Trending', 'Trending')], max_length=100)),
                ('Main_post', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='HOME.category')),
            ],
        ),
    ]
