# Generated by Django 3.2.5 on 2021-07-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em', models.CharField(max_length=10, unique=True)),
                ('pws', models.CharField(max_length=256)),
            ],
        ),
    ]
