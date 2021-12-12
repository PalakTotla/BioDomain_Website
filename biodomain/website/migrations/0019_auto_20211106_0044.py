# Generated by Django 3.2.8 on 2021-11-05 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20211106_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruments',
            name='Category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.category_description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instruments',
            name='Institute',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.institute'),
            preserve_default=False,
        ),
    ]
