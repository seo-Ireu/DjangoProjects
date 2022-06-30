# Generated by Django 2.2.6 on 2019-10-29 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='file',
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('desc', models.CharField(max_length=100)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]