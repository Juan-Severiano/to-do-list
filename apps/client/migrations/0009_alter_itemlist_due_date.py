# Generated by Django 4.2.2 on 2023-06-08 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_alter_itemlist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
