# Generated by Django 4.2.5 on 2023-10-08 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Зірка рейтингу', 'verbose_name_plural': 'Зірки рейтингу'},
        ),
    ]
