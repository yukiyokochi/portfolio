# Generated by Django 3.1.1 on 2020-09-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0003_auto_20200918_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='特記事項やアレルギー等'),
        ),
    ]
