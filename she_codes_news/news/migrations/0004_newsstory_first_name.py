# Generated by Django 4.1.3 on 2022-12-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]