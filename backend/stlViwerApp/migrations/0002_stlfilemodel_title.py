# Generated by Django 3.2.7 on 2021-09-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stlViwerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stlfilemodel',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
