# Generated by Django 3.0.1 on 2020-02-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20200218_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='status',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=10, verbose_name='status'),
        ),
    ]
