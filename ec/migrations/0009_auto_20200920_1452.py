# Generated by Django 3.1.1 on 2020-09-20 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0008_auto_20200920_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicelocation',
            name='mustorderprice',
        ),
        migrations.RemoveField(
            model_name='choicelocation',
            name='shippingtax',
        ),
        migrations.RemoveField(
            model_name='choicelocation',
            name='shippingtime',
        ),
    ]
