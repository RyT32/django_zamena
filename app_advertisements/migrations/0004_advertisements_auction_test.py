# Generated by Django 3.2.20 on 2023-07-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_alter_advertisements_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='auction_test',
            field=models.BooleanField(default=False, help_text='Возможен торг или нет', verbose_name='торг2'),
        ),
    ]
