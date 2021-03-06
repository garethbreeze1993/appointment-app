# Generated by Django 3.0.2 on 2020-01-07 16:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(choices=[(datetime.time(9, 0), '9AM'), (datetime.time(10, 0), '10AM'), (datetime.time(11, 0), '11AM')])),
                ('date_start', models.DateField()),
                ('time_end', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.AddConstraint(
            model_name='times',
            constraint=models.UniqueConstraint(fields=('time_start', 'date_start'), name='unique_datetime'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='times',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='appointment_app.Times'),
        ),
    ]
