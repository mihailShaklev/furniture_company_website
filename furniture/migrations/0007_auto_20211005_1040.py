# Generated by Django 3.1.5 on 2021-10-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0006_auto_20211005_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_1',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_2',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_3',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_4',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_5',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_6',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(default='null', upload_to='furniture/static/furniture/uploads/images'),
        ),
    ]
