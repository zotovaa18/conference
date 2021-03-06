# Generated by Django 4.0.5 on 2022-07-07 20:47

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SectionNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SlugField(max_length=2, unique=True, verbose_name='Номер секции')),
                ('name', models.TextField(unique=True, verbose_name='Полное название')),
                ('сhairman', models.TextField(null=True, verbose_name='Председатель секции')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секции',
            },
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, verbose_name='Код рубрики')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('title', models.TextField(verbose_name='Название доклада')),
                ('file1', models.FileField(upload_to='files/', verbose_name='Файл с тезисами')),
                ('file2', models.FileField(upload_to='files/', verbose_name='Файл с подписью научного руководителя')),
                ('cont_fio', models.CharField(help_text='ФИО контактного лица', max_length=150, verbose_name='Контактное лицо')),
                ('cont_phone_number', phone_field.models.PhoneField(help_text='Номер телефона контактного лица', max_length=31, verbose_name='Телефон')),
                ('cont_email', models.EmailField(help_text='Электронный адрес контактного лица', max_length=254, verbose_name='Email')),
                ('cleaver', models.CharField(choices=[('да', 'Да'), ('нет', 'Нет')], default='нет', max_length=3, verbose_name='УМНИК')),
                ('name_project', models.TextField(blank=True, null=True, verbose_name='Название проекта')),
                ('aim', models.TextField(blank=True, null=True, verbose_name='Цель выполнения НИР')),
                ('purpose', models.TextField(blank=True, null=True, verbose_name='Назначение научно-технического продукта')),
                ('novelty', models.TextField(blank=True, null=True, verbose_name='Научная новизна предлагаемых в проекте решений')),
                ('justification', models.TextField(blank=True, null=True, verbose_name='Обоснование необходимости проведения НИР')),
                ('options', models.TextField(blank=True, null=True, verbose_name='Основные технические параметры, определяющие количественные, качественные и стоимостные характеристики продукции')),
                ('requirements', models.TextField(blank=True, null=True, verbose_name='Конструктивные требования')),
                ('protection', models.TextField(blank=True, null=True, verbose_name='Требования по патентной защите')),
                ('application', models.TextField(blank=True, null=True, verbose_name='Область применения')),
                ('budget', models.TextField(blank=True, null=True, verbose_name='Объем внебюджетных инвестиций или собственных средств')),
                ('analogue', models.TextField(blank=True, null=True, verbose_name='Имеющиеся аналоги')),
                ('plan', models.TextField(blank=True, null=True, verbose_name='План реализации')),
                ('sec_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_data.sectionnumber', verbose_name='Номер секции')),
            ],
            options={
                'verbose_name': 'Тезис',
                'verbose_name_plural': 'Тезисы',
            },
        ),
        migrations.CreateModel(
            name='ScientificDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО полностью')),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
                ('thesis', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='user_data.thesis', verbose_name='Тезис')),
            ],
            options={
                'verbose_name': 'Научный руководитель',
                'verbose_name_plural': 'Научные руководители',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_short', models.CharField(max_length=100, verbose_name='ФИО фамилия, инициалы')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО полностью')),
                ('date_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('status', models.TextField(verbose_name='Статус')),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('organization', models.TextField(verbose_name='Организация')),
                ('faculty', models.TextField(verbose_name='Факультет')),
                ('department', models.TextField(verbose_name='Департамент')),
                ('city', models.TextField(verbose_name='Город')),
                ('thesis', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='user_data.thesis', verbose_name='Тезис')),
            ],
            options={
                'verbose_name': 'Автор доклада',
                'verbose_name_plural': 'Авторы доклада',
            },
        ),
    ]
