# Generated by Django 4.1.7 on 2023-03-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('consumer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consumer.consumer')),
            ],
        ),
    ]
