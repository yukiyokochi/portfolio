# Generated by Django 3.1.1 on 2020-09-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0007_choicelocation_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicelocation',
            name='mustorderprice',
            field=models.IntegerField(null=True, verbose_name='必要注文最低額'),
        ),
        migrations.AddField(
            model_name='choicelocation',
            name='shippingtax',
            field=models.IntegerField(null=True, verbose_name='送料'),
        ),
        migrations.AddField(
            model_name='choicelocation',
            name='shippingtime',
            field=models.IntegerField(null=True, verbose_name='配達所要時間(分)'),
        ),
    ]
