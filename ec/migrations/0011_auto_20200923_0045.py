# Generated by Django 3.1.1 on 2020-09-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0010_menu_soldout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='soldout',
            field=models.IntegerField(blank=True, choices=[(0, '販売中'), (1, '売り切れ中')], null=True, verbose_name='販売状況'),
        ),
    ]
