# Generated by Django 4.2.2 on 2023-06-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_itemlist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('DOING', 'Doing'), ('DONE', 'Done')], max_length=5),
        ),
    ]
