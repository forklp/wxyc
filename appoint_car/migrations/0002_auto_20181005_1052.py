# Generated by Django 2.0.4 on 2018-10-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint_car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='taxi',
            new_name='driver',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(choices=[(0, '未分配'), (1, '分配')], default=0),
        ),
    ]