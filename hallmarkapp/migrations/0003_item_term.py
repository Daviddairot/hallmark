# Generated by Django 4.2.6 on 2023-10-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hallmarkapp', '0002_item_book_description_item_content_1_item_content_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='term',
            field=models.CharField(max_length=100, null=True),
        ),
    ]