# Generated by Django 3.0.2 on 2020-02-01 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_posts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelTable(
            name='posts',
            table='Posts',
        ),
    ]
