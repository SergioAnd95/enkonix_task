# Generated by Django 2.2.6 on 2019-10-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
