# Generated by Django 4.2.5 on 2023-10-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('products_id', models.AutoField(primary_key=True, serialize=False)),
                ('products_status', models.CharField(choices=[('1', 'arrival'), ('2', 'in-store'), ('3', 'dispatch')], max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('SKU', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('arrival_date', models.DateField()),
                ('dispatch_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
