# Generated by Django 2.1.1 on 2019-03-19 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0003_auto_20190319_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.ImageField(upload_to='eshop/uploads'),
        ),
    ]