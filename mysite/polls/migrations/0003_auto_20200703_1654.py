# Generated by Django 3.0.8 on 2020-07-03 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
