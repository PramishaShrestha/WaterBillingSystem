# Generated by Django 4.1.7 on 2023-05-05 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumer_profile',
            old_name='consumerobj',
            new_name='consumer',
        ),
    ]
