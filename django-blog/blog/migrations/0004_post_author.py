# Generated by Django 3.2.25 on 2025-02-28 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]
