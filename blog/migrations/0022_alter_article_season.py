# Generated by Django 4.1.6 on 2023-02-14 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_article_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='season',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.season'),
            preserve_default=False,
        ),
    ]
