# Generated by Django 4.1.7 on 2023-03-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_title_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
