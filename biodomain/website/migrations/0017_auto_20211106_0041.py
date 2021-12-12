# Generated by Django 3.2.8 on 2021-11-05 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20211106_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruments',
            name='Category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.category_description'),
        ),
        migrations.AlterField(
            model_name='instruments',
            name='Institute',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.institute'),
        ),
    ]
