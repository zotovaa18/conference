from datetime import date

from django.db import models

# Create your models here.
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file1_extension, validate_file2_extension


class SectionNumber(models.Model):
    """Секции"""
    number = models.CharField("Номер секции", max_length=2, unique=True)
    name = models.TextField("Полное название", unique=True)
    сhairman = models.TextField("Председатель секции", null=True)

    def __str__(self):
        return f"Секция {self.number}. {self.name}"

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"


class Thesis(models.Model):
    """Тезисы"""
    CHOICES = (
        ('да', 'Да'),
        ('нет', 'Нет'),
    )

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    sec_num = models.ForeignKey(SectionNumber, verbose_name="Номер секции", on_delete=models.CASCADE, null=False)
    code = models.CharField("Код рубрики", max_length=50, help_text='Пример: 12.33.21, 33.23.11')
    comment = models.TextField("Комментарий", blank=True, null=True)
    title = models.TextField("Название доклада", null=False)
    file1 = models.FileField("Файл с тезисами", upload_to="files/", validators=[validate_file1_extension], null=False)
    file2 = models.FileField("Файл с подписью научного руководителя", upload_to="files/", 
                             validators=[validate_file2_extension], null=False)
    cont_fio = models.CharField("Контактное лицо", max_length=150, help_text='Пример: Иванов Сергей Михайлович')
    cont_phone_number = PhoneNumberField("Телефон", help_text='Пример: +79160003333', max_length=12)
    cont_email = models.EmailField("Email", help_text='Пример: mail@hse.ru')
    cleaver = models.CharField("УМНИК", max_length=3, choices=CHOICES, default="нет", null=False)
    name_project = models.TextField("Название проекта", blank=True, null=True)
    aim = models.TextField("Цель выполнения НИР", blank=True, null=True)
    purpose = models.TextField("Назначение научно-технического продукта", blank=True, null=True)
    novelty = models.TextField("Научная новизна предлагаемых в проекте решений", blank=True, null=True)
    justification = models.TextField("Обоснование необходимости проведения НИР", blank=True, null=True)
    options = models.TextField("Основные технические параметры, определяющие количественные, качественные и стоимостные характеристики продукции", blank=True, null=True)
    requirements = models.TextField("Конструктивные требования", blank=True, null=True)
    protection = models.TextField("Требования по патентной защите", blank=True, null=True)
    application = models.TextField("Область применения", blank=True, null=True)
    budget = models.PositiveIntegerField("Объем внебюджетных инвестиций или собственных средств", blank=True, null=True)
    analogue = models.TextField("Имеющиеся аналоги", blank=True, null=True)
    plan = models.TextField("План реализации", blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Тезис"
        verbose_name_plural = "Тезисы"


class ScientificDirector(models.Model):
    """Научный руководитель доклада"""
    fio = models.CharField("ФИО полностью", max_length=150, help_text='Пример: Иванов Сергей Михайлович')
    phone_number = PhoneNumberField("Телефон", blank=True, null=True, help_text='Пример: +79160003333', max_length=12)
    email = models.EmailField("Email", help_text='Пример: mail@hse.ru')
    thesis = models.OneToOneField(Thesis, on_delete=models.CASCADE, verbose_name="Тезис", related_name="director")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Научный руководитель"
        verbose_name_plural = "Научные руководители"


class Author(models.Model):
    """Авторы"""
    fio_short = models.CharField("ФИО фамилия, инициалы", max_length=100, help_text='Пример: Иванов С.М.')
    fio = models.CharField("ФИО полностью", help_text='Пример: Иванов Сергей Михайлович', max_length=150)
    date_birth = models.DateField("Дата рождения", null=True)
    status = models.TextField("Статус", help_text='Пример: бакалавр 3 курс')
    phone_number = PhoneNumberField("Телефон", help_text='Пример: +79160003333', max_length=12)
    email = models.EmailField("Email", help_text='Пример: mail@hse.ru')
    organization = models.TextField("Организация", help_text='Пример: НИУ ВШЭ')
    faculty = models.TextField("Факультет", help_text='Пример: МИЭМ НИУ ВШЭ')
    department = models.TextField("Департамент")
    city = models.TextField("Город")
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, verbose_name="Тезис", related_name="authors",
                               null=False)

    def __str__(self):
        return self.fio_short

    class Meta:
        verbose_name = "Автор доклада"
        verbose_name_plural = "Авторы доклада"


class ThesisAll(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    code = models.CharField("Код рубрики", max_length=50, default='')
    comment = models.TextField("Комментарий", blank=True, null=True)
    number = models.CharField("Номер секции", max_length=2, default='')
    title = models.TextField("Название доклада")
    authors = models.TextField("Авторы тезиса", blank=True, null=True)
    cont_fio = models.CharField("Контактное лицо", max_length=150, help_text='ФИО контактного лица')
    cont_phone_number = PhoneNumberField("Телефон", help_text='Номер телефона контактного лица', max_length=12)
    cont_email = models.EmailField("Email", help_text='Электронный адрес контактного лица')
    status = models.TextField("Статус авторов", blank=True, null=True)
    phone_author = models.TextField("Телефоны авторов", blank=True, null=True)
    email_authors = models.TextField("Почты авторов", blank=True, null=True)
    organization = models.TextField("Организация", blank=True, null=True)
    faculty = models.TextField("Факультет", blank=True, null=True)
    department = models.TextField("Департамент", blank=True, null=True)
    city = models.TextField("Город", blank=True, null=True)
    fio_dir = models.CharField("Научный руководитель", max_length=150)
    phone_number_dir = PhoneNumberField("Телефон научного руководителя", blank=True, null=True,
                                        help_text='Пример: +79160003333', max_length=12)
    email_dir = models.EmailField("Email научного руководителя", help_text='Пример: mail@hse.ru')
    cleaver = models.CharField("УМНИК", max_length=3)
    name_project = models.TextField("Название проекта", blank=True, null=True)
    aim = models.TextField("Цель выполнения НИР", blank=True, null=True)
    purpose = models.TextField("Назначение научно-технического продукта", blank=True, null=True)
    novelty = models.TextField("Научная новизна предлагаемых в проекте решений", blank=True, null=True)
    justification = models.TextField("Обоснование необходимости проведения НИР", blank=True, null=True)
    options = models.TextField(
        "Основные технические параметры, определяющие количественные, качественные и стоимостные характеристики продукции",
        blank=True, null=True)
    requirements = models.TextField("Конструктивные требования", blank=True, null=True)
    protection = models.TextField("Требования по патентной защите", blank=True, null=True)
    application = models.TextField("Область применения", blank=True, null=True)
    budget = models.PositiveIntegerField("Объем внебюджетных инвестиций или собственных средств", blank=True,
                                         null=True)
    analogue = models.TextField("Имеющиеся аналоги", blank=True, null=True)
    plan = models.TextField("План реализации", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_thesis'
