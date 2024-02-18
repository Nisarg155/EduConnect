# Generated by Django 5.0 on 2024-02-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0002_alter_class_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
            ],
        ),
    ]
