# Generated by Django 3.1 on 2020-08-25 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud_proyecto', '0008_auto_20200824_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_proyecto',
            name='tags',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
