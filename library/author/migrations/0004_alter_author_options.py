# Generated by Django 4.1 on 2022-11-19 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_alter_author_books_alter_author_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автори', 'verbose_name_plural': 'Автори'},
        ),
    ]
