# Generated by Django 2.2.15 on 2021-05-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210513_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='seniorinfo',
            name='description2',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
