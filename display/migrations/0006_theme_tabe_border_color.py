# Generated by Django 3.1.5 on 2021-03-25 13:46

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0005_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='Tabe_Border_Color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]
