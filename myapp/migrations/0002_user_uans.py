# Generated by Django 3.0.8 on 2020-07-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uans',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
