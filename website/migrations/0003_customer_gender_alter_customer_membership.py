# Generated by Django 4.2.4 on 2023-08-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_customeraddress_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('S', 'Silver'), ('G', 'Gold'), ('B', 'Bronze')], default='B', max_length=1),
        ),
    ]
