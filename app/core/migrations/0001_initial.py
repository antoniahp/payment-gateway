# Generated by Django 4.1.2 on 2023-10-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethodDataBankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('cvc', models.IntegerField()),
                ('date_of_expire', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethodDataBizum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethodDataPayPal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
