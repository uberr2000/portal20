# Generated by Django 3.0.1 on 2020-01-08 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20200103_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='quality',
            field=models.CharField(default='', max_length=4, verbose_name='資料集品質'),
        ),
    ]