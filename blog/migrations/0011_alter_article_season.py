# Generated by Django 4.1.6 on 2023-02-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_article_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.season'),
        ),
    ]
