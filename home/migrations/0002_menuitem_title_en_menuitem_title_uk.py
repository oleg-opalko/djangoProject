# Generated by Django 5.1.3 on 2024-11-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_uk',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
