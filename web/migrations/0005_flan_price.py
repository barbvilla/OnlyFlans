# Generated by Django 3.2.4 on 2022-03-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
