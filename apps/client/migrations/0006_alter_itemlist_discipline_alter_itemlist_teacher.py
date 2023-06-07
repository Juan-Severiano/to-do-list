# Generated by Django 4.2.2 on 2023-06-07 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_itemlist_discipline_alter_itemlist_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.discipline'),
        ),
        migrations.AlterField(
            model_name='itemlist',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.teacher'),
        ),
    ]
