# Generated by Django 4.0.5 on 2022-07-17 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cart_options_alter_item_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '明細注文', 'verbose_name_plural': '明細注文'},
        ),
    ]