# Generated by Django 4.0.5 on 2022-07-09 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vols', '0002_sentence_chinese'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='ans',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
