# Generated by Django 4.0.4 on 2022-05-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
