# Generated by Django 2.1.7 on 2021-03-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/profile_pics/1439536495-1_szqxjfg.png', upload_to='profile_pics'),
        ),
    ]