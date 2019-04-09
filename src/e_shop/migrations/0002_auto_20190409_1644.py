# Generated by Django 2.1.1 on 2019-04-09 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='is_executed',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]