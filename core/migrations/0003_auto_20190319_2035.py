# Generated by Django 2.1.7 on 2019-03-20 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='user_fav',
            new_name='favorite',
        ),
    ]
