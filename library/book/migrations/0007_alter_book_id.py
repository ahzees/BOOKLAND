# Generated by Django 4.1 on 2022-11-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_merge_0003_alter_book_id_0005_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
