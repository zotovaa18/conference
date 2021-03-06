# Generated by Django 4.0.5 on 2022-07-14 21:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0008_alter_author_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThesisAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, verbose_name='Код рубрики')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('number', models.CharField(default='', max_length=2, verbose_name='Номер секции')),
                ('title', models.TextField(verbose_name='Название доклада')),
                ('cont_fio', models.CharField(help_text='ФИО контактного лица', max_length=150, verbose_name='Контактное лицо')),
                ('cont_phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона контактного лица', max_length=12, region=None, verbose_name='Телефон')),
                ('cont_email', models.EmailField(help_text='Электронный адрес контактного лица', max_length=254, verbose_name='Email')),
                ('authors', models.TextField(blank=True, null=True, verbose_name='Авторы')),
                ('status', models.TextField(blank=True, null=True, verbose_name='Статус')),
                ('phone_author', models.TextField(blank=True, null=True, verbose_name='Телефоны авторов')),
                ('email_authors', models.TextField(blank=True, null=True, verbose_name='Почты авторов')),
                ('organization', models.TextField(blank=True, null=True, verbose_name='Организация')),
                ('faculty', models.TextField(blank=True, null=True, verbose_name='Факультет')),
                ('department', models.TextField(blank=True, null=True, verbose_name='Департамент')),
                ('city', models.TextField(blank=True, null=True, verbose_name='Город')),
                ('fio_dir', models.CharField(max_length=150, verbose_name='Научный руководитель')),
                ('phone_number_dir', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=12, null=True, region=None, verbose_name='Телефон научного руководителя')),
                ('email_dir', models.EmailField(max_length=254, verbose_name='Email научного руководителя')),
                ('cleaver', models.CharField(max_length=3, verbose_name='УМНИК')),
                ('name_project', models.TextField(blank=True, null=True, verbose_name='Название проекта')),
                ('aim', models.TextField(blank=True, null=True, verbose_name='Цель выполнения НИР')),
                ('purpose', models.TextField(blank=True, null=True, verbose_name='Назначение научно-технического продукта')),
                ('novelty', models.TextField(blank=True, null=True, verbose_name='Научная новизна предлагаемых в проекте решений')),
                ('justification', models.TextField(blank=True, null=True, verbose_name='Обоснование необходимости проведения НИР')),
                ('options', models.TextField(blank=True, null=True, verbose_name='Основные технические параметры, определяющие количественные, качественные и стоимостные характеристики продукции')),
                ('requirements', models.TextField(blank=True, null=True, verbose_name='Конструктивные требования')),
                ('protection', models.TextField(blank=True, null=True, verbose_name='Требования по патентной защите')),
                ('application', models.TextField(blank=True, null=True, verbose_name='Область применения')),
                ('budget', models.PositiveIntegerField(blank=True, null=True, verbose_name='Объем внебюджетных инвестиций или собственных средств')),
                ('analogue', models.TextField(blank=True, null=True, verbose_name='Имеющиеся аналоги')),
                ('plan', models.TextField(blank=True, null=True, verbose_name='План реализации')),
            ],
            options={
                'db_table': 'thesis_all',
                'managed': False,
            },
        ),
    ]
