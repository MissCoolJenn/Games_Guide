# Generated by Django 4.1.7 on 2023-05-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
