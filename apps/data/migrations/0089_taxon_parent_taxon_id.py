# Generated by Django 4.0 on 2023-04-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0088_taxon_class_taxon_id_taxon_family_taxon_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxon',
            name='parent_taxon_id',
            field=models.CharField(max_length=256, null=True, verbose_name='self'),
        ),
    ]