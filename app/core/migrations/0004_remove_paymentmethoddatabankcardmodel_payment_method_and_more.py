# Generated by Django 4.1.2 on 2023-10-16 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_name_paymentmethoddatabankcardmodel_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethoddatabankcardmodel',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='paymentmethoddatabizummodel',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='paymentmethoddatapaypalmodel',
            name='payment_method',
        ),
    ]
