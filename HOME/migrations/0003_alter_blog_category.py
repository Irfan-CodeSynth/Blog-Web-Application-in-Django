# Generated by Django 5.1 on 2024-08-11 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_alter_blog_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='HOME.category'),
        ),
    ]
