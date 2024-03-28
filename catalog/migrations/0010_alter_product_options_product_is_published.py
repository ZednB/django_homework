# Generated by Django 4.2 on 2024-03-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('is_published', 'может отменять публикацию продукта'), ('can_change_description', 'может менять описание любого продукта'), ('can_change_category', 'может менять категорию любого продукта')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
    ]