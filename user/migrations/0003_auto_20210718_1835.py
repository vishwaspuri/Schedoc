# Generated by Django 3.2.5 on 2021-07-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auth'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em', models.CharField(max_length=256)),
                ('otp', models.IntegerField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='auth',
            name='em',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]