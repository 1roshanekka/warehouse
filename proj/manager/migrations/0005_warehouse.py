# Generated by Django 4.2.5 on 2023-10-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
