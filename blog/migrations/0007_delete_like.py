# Generated by Django 4.1.6 on 2023-02-12 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_like_article_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
