# Generated by Django 4.1.4 on 2022-12-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facial', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authentication',
            options={'verbose_name': 'Auth', 'verbose_name_plural': 'Authentications'},
        ),
        migrations.AddField(
            model_name='authentication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]