# Generated by Django 4.0.3 on 2022-03-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_doctor_degree_patient_phone_alter_doctor_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='degree',
            field=models.CharField(default='Working', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='job',
            field=models.CharField(default='Working', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='special',
            field=models.CharField(default='General', max_length=100),
        ),
    ]
