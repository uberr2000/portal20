# Generated by Django 3.2.5 on 2021-08-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0047_auto_20200720_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='extension_data',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='count',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='hierarchy_string',
            field=models.CharField(default='', max_length=512, null=True, verbose_name='hierarchy string'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='name_zh',
            field=models.CharField(max_length=128, null=True, verbose_name='name_zh'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='verbose',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='verbose'),
        ),
    ]