# Generated by Django 4.1 on 2022-11-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_alter_book_year_of_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]