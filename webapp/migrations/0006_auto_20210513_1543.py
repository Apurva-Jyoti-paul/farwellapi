# Generated by Django 2.2.15 on 2021-05-13 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_seniorinfo_description2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='desc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gall', to='webapp.Seniorinfo'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='senior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rat', to='webapp.Seniorinfo'),
        ),
    ]
