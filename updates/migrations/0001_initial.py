# Generated by Django 3.2.4 on 2021-06-14 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_tg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
            ],
        ),
    ]
