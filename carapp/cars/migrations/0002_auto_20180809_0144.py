# Generated by Django 2.0.5 on 2018-08-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pix', verbose_name='Main Photo'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='pix'),
        ),
    ]