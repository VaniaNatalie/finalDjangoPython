# Generated by Django 3.1.3 on 2020-12-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201223_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='account_pics'),
        ),
    ]