# Generated by Django 4.1.7 on 2023-03-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0005_remove_consumer_consumer_id_alter_consumer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='consumer_id',
            field=models.IntegerField(default=8090),
            preserve_default=False,
        ),
    ]
