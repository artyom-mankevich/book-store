# Generated by Django 4.0.1 on 2022-01-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=4, null=True),
        ),
    ]