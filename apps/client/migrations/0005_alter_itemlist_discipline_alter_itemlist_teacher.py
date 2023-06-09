# Generated by Django 4.2.2 on 2023-06-07 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_itemlist_discipline_alter_itemlist_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='discipline',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='client.discipline'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemlist',
            name='teacher',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='client.teacher'),
            preserve_default=False,
        ),
    ]
