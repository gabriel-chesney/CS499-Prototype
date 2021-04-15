# Generated by Django 3.1.5 on 2021-04-14 13:18

from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0011_auto_20210408_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='recDate',
            field=recurrence.fields.RecurrenceField(),
        ),
    ]