# Generated by Django 4.0 on 2023-06-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0097_taxon_taicol_synonyms_alter_taxon_is_accepted_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxon',
            name='alien_type',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='alien_type'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='alternative_name_c',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='alternative_name_c'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='cites',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='cites'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='formatted_misapplied',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='formatted_misapplied'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='formatted_synonyms',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='formatted_synonyms'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='misapplied',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='misapplied'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='taicol_synonyms',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='synonyms'),
        ),
    ]