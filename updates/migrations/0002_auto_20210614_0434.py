# Generated by Django 3.2.4 on 2021-06-14 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tg',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_tg',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
