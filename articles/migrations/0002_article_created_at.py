# Generated by Django 5.1.4 on 2024-12-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
