# Generated by Django 4.0 on 2022-09-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0080_alter_dataset_description_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='is_most_project',
            field=models.BooleanField(default=False, verbose_name='是否為國科會計畫'),
        ),
    ]
