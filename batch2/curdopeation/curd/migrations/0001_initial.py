# Generated by Django 5.2.4 on 2025-07-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('productprice', models.CharField(max_length=100)),
                ('productdist', models.CharField(max_length=100)),
            ],
        ),
    ]
