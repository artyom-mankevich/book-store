# Generated by Django 4.0.1 on 2022-01-20 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_book_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory'),
        ),
    ]
