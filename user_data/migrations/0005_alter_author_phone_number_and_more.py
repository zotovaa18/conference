# Generated by Django 4.0.5 on 2022-07-10 17:00

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0004_alter_sectionnumber_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone_number',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='scientificdirector',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=12, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='cont_phone_number',
            field=phone_field.models.PhoneField(help_text='Номер телефона контактного лица', max_length=12, verbose_name='Телефон'),
        ),
    ]
