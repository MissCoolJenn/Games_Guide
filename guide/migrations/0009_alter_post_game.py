# Generated by Django 4.1.7 on 2023-05-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0008_alter_post_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='game',
            field=models.CharField(choices=[('NON', 'None'), ('TAR', 'Escape From Tarkov'), ('OOO', 'Test')], default='None', max_length=3),
        ),
    ]