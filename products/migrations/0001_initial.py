# Generated by Django 4.0.1 on 2022-01-13 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100, verbose_name='Country that is associated with the author')),
                ('birth_date', models.DateField(null=True)),
                ('death_date', models.DateField(null=True)),
                ('description', models.TextField(null=True)),
                ('rating', models.DecimalField(decimal_places=2, editable=False, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, editable=False, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='International Standard Book Number')),
                ('title', models.CharField(max_length=100, verbose_name="book's title")),
                ('cover', models.CharField(choices=[('H', 'Hard'), ('S', 'Soft')], max_length=1, verbose_name='a type of book cover, either soft or hard')),
                ('dimensions', models.CharField(max_length=15, verbose_name="Book's dimensions")),
                ('description', models.TextField(blank=True, verbose_name="Book's description")),
                ('price', models.DecimalField(decimal_places=4, max_digits=13, verbose_name="book's price in decimal")),
                ('year', models.SmallIntegerField(verbose_name='publication year')),
                ('pages', models.SmallIntegerField(verbose_name='amount of pages in a book')),
                ('available_count', models.SmallIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, editable=False, max_digits=4)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.publisher')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory')),
            ],
        ),
    ]
