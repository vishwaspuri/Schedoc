# Generated by Django 3.2.5 on 2021-07-11 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.utils.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('prescription', models.TextField(max_length=256, null=True)),
                ('payment', models.FloatField(default=0)),
                ('payment_paid', models.BooleanField(default=False)),
                ('feedback', models.TextField(max_length=256, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient_appointments', to=settings.AUTH_USER_MODEL, validators=[user.utils.user.validate_doctor])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
