# Generated by Django 2.2.6 on 2019-10-29 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20191029_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='myfile',
        ),
    ]
