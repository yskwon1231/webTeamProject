# Generated by Django 2.1.2 on 2018-12-05 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0002_auto_20181108_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='take',
            name='take_end',
        ),
        migrations.RemoveField(
            model_name='take',
            name='take_start',
        ),
        migrations.AlterField(
            model_name='take',
            name='u_id',
            field=models.CharField(max_length=10),
        ),
    ]