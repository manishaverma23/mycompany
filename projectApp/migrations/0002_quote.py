# Generated by Django 5.0.1 on 2024-02-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
