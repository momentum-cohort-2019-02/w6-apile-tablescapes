# Generated by Django 2.1.7 on 2019-03-25 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190325_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_post',
            new_name='post',
        ),
    ]
