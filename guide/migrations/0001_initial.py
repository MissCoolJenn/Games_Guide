# Generated by Django 4.1.7 on 2023-03-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
