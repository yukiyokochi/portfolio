# Generated by Django 3.1 on 2020-12-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_form_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='location',
            field=models.CharField(default=2, max_length=255, verbose_name='エリア'),
            preserve_default=False,
        ),
    ]
