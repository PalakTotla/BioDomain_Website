# Generated by Django 3.2.8 on 2021-11-05 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_category_description_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_description',
            old_name='Category_Description',
            new_name='Description',
        ),
    ]
