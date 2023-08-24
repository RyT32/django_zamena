# Generated by Django 3.2.20 on 2023-08-05 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisements', '0009_rename_descriptoin_advertisements_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
