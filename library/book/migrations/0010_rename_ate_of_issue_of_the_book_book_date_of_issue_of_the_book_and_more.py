# Generated by Django 4.1 on 2022-11-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_book_ate_of_issue_of_the_book_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ate_of_issue_of_the_book',
            new_name='date_of_issue_of_the_book',
        ),
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True),
        ),
    ]