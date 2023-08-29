# Generated by Django 4.2.4 on 2023-08-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerAddress',
            new_name='Address',
        ),
        migrations.AlterField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('G', 'Gold'), ('B', 'Bronze'), ('S', 'Silver')], default='B', max_length=1),
        ),
    ]
