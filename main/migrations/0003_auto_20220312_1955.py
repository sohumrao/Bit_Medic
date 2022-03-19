# Generated by Django 3.2.8 on 2022-03-13 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220312_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='owner',
        ),
        migrations.AddField(
            model_name='document',
            name='patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.patient'),
        ),
    ]
