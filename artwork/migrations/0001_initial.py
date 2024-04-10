# Generated by Django 5.0.4 on 2024-04-09 00:02

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]