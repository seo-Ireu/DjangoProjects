# Generated by Django 2.2.1 on 2019-05-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryApp', '0002_diary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='image',
            field=models.ImageField(default='images/p', upload_to='images/'),
        ),
    ]
