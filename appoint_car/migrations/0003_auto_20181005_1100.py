# Generated by Django 2.0.4 on 2018-10-05 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint_car', '0002_auto_20181005_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(choices=[(0, '未分配'), (1, '已分配')], default=0),
        ),
    ]
