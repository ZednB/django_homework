# Generated by Django 5.0.2 on 2024-03-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_created_date_alter_product_uploaded_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='version_sign',
            new_name='is_active',
        ),
    ]
