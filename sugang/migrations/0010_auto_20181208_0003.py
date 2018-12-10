# Generated by Django 2.1.2 on 2018-12-07 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0009_auto_20181207_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='i_code',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='i_code',
        ),
        migrations.RemoveField(
            model_name='take',
            name='sub_code',
        ),
        migrations.AddField(
            model_name='take',
            name='subject_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sugang.Subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='i_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sugang.Instructor'),
        ),
    ]
