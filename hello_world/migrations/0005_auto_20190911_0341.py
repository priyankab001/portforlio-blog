# Generated by Django 2.2.3 on 2019-09-11 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0004_auto_20190910_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/img'),
        ),
    ]
