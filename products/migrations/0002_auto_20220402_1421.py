# Generated by Django 3.2 on 2022-04-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishescategory',
            name='friendly_name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='dishescategory',
            name='name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='winecategory',
            name='friendly_name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='winecategory',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
