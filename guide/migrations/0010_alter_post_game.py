# Generated by Django 4.1.7 on 2023-05-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_alter_post_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='game',
            field=models.CharField(choices=[('EscapeFromTarkov', 'Escape From Tarkov'), ('Test', 'Test')], max_length=50),
        ),
    ]
