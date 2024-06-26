# Generated by Django 5.0.1 on 2024-06-12 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products_principal',
            fields=[
                ('product_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventories_principal',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_quantity', models.IntegerField()),
                ('date_entry', models.DateField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.products_principal')),
            ],
        ),
        migrations.CreateModel(
            name='Sales_principal',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('quantity', models.SmallIntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.products_principal')),
            ],
        ),
    ]
