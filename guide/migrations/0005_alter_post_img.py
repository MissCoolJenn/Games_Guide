# Generated by Django 4.1.7 on 2023-04-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0004_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
