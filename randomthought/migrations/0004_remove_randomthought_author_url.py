# Generated by Django 4.0.3 on 2022-04-03 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomthought', '0003_randomthought_author_url_alter_randomthought_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randomthought',
            name='author_url',
        ),
    ]
