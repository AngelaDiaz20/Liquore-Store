# Generated by Django 3.2.8 on 2021-10-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquore_store_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripción',
            field=models.CharField(default=12, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='grados',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]
