# Generated by Django 5.1 on 2024-08-11 10:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='HOME.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='HOME.blog')),
            ],
        ),
    ]
