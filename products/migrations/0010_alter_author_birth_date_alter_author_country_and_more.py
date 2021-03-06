# Generated by Django 4.0.1 on 2022-01-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_author_slug_publisher_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country that is associated with the author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
