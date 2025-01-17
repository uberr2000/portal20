# Generated by Django 4.0 on 2023-06-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0096_remove_taxon_hierarchy_string_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxon',
            name='taicol_synonyms',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='synonyms'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='is_accepted_name',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
    ]
