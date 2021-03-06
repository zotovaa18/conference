# Generated by Django 4.0.5 on 2022-07-07 21:33

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0002_alter_thesis_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone_number',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='scientificdirector',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
