# Generated by Django 4.2.1 on 2023-05-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=255)),
                ('order_date', models.DateField()),
                ('ship_date', models.DateField()),
                ('ship_mode', models.CharField(max_length=255)),
                ('customer_id', models.CharField(max_length=255)),
                ('customer_name', models.CharField(max_length=255)),
                ('segment', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sub_category', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('sales', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
