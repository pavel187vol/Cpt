# Generated by Django 3.0.1 on 2020-01-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200104_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, default='/order_default.png', upload_to='orders'),
        ),
    ]