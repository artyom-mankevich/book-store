# Generated by Django 4.0.1 on 2022-01-20 15:35

from django.db import migrations, models
import django.db.models.deletion
import products.utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('H', 'Hard'), ('S', 'Soft')], max_length=1, verbose_name='a type of book cover'),
        ),
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.utils.book_directory_path)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='main_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='products.bookimage'),
        ),
    ]
