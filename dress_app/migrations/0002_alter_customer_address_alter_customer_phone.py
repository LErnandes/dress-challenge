# Generated by Django 4.0 on 2021-12-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dress_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ManyToManyField(blank=True, to='dress_app.Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.ManyToManyField(blank=True, to='dress_app.Phone'),
        ),
    ]
