# Generated by Django 3.1 on 2020-12-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='支払い方法')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='お名前')),
                ('address', models.CharField(max_length=64, verbose_name='ご住所')),
                ('tel', models.CharField(max_length=255, verbose_name='電話番号')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('text', models.CharField(blank=True, max_length=512, verbose_name='備考')),
                ('payway', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.payment', verbose_name='支払い方法')),
            ],
        ),
    ]
