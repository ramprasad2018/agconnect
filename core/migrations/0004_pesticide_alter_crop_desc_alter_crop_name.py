# Generated by Django 4.1.7 on 2023-03-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_description_crop_desc_remove_crop_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('type', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='crop',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
    ]
