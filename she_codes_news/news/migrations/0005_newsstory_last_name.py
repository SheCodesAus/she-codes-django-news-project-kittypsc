# Generated by Django 4.1.3 on 2022-12-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsstory_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
