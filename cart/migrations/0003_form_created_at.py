# Generated by Django 3.1 on 2020-12-14 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_form_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='注文日時'),
        ),
    ]
