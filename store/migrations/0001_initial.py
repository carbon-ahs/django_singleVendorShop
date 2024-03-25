# Generated by Django 4.0 on 2024-03-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('model', models.CharField(max_length=50, verbose_name='Model')),
                ('purchase_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('current_market_price', models.IntegerField()),
                ('release_date', models.DateTimeField()),
                ('specification', models.TextField()),
                ('image', models.ImageField(default='assets/img/stock_images/default_phone_image_low_quality.jpg', upload_to='product_img/')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
