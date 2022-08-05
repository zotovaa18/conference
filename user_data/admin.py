from django.contrib import admin
from .models import SectionNumber, Author, ScientificDirector, Thesis, ThesisAll
from django.template.loader import get_template
from user_data.forms import ThesisForm
from django.utils.safestring import mark_safe
from django.contrib.admin.options import TabularInline
from django.views.generic import ListView

import xlwt
import datetime
from django.http import HttpResponse


# Register your models here.


@admin.register(SectionNumber)
class SectionNumberAdmin(admin.ModelAdmin):
    """Секции"""
    list_display = ("number", "name", "сhairman")
    list_display_links = ("number",)


# TabularInline тогда все отзывы будут по горизонтали в таблице
class AuthorInline(admin.StackedInline):
    """Авторы на странице тезиса"""
    model = Author
    classes = ['collapse']
    extra = 1

class ScientificDirectorInline(admin.StackedInline):
    """Данные научного руководителя на странице тезиса"""
    model = ScientificDirector
    classes = ['collapse']
    extra = 1


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    """Тезисы"""

    list_display = ("id", "code", "comment", "title", "sec_num", "file1", "file2", "author_inline_show",
                    "cont_fio", "cont_phone_number", "cont_email","author_inline_status", "author_inline_organization",
                    "author_inline_faculty", "author_inline_department", "author_inline_city",
                    "scientific_director_inline_show", "cleaver", "name_project", "aim", "purpose",
                    "novelty", "justification", "options", "requirements","protection", "application", "budget",
                    "analogue", "plan")

    list_filter = ("sec_num",) # фильтрация по категориям
    search_fields = ("authors__fio_short__iregex", "id",) # поиск
    inlines = (AuthorInline, ScientificDirectorInline)
    save_on_top = True #кнопка сохранить сверху теперь
    readonly_fields = ('author_inline', 'scientific_director_inline') # method as readonly field
    actions = ["download_thesis", ]

    def author_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {} # sometimes context.copy() is better
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    def author_inline_show(self, obj):
        a = "<br>"
        return mark_safe(a.join([ author.fio_short for author in Author.objects.filter(thesis=obj.id) ]))

    def author_inline_status(self, obj):
        a = "<br>"
        return mark_safe(a.join([ author.status for author in Author.objects.filter(thesis=obj.id) ]))

    def author_inline_organization(self, obj):
        a = "<br>"
        return mark_safe(a.join([ author.organization for author in Author.objects.filter(thesis=obj.id) ]))

    def author_inline_faculty(self, obj):
        a = "<br>"
        return mark_safe(a.join([ author.faculty for author in Author.objects.filter(thesis=obj.id) ]))

    def author_inline_department(self, obj):
        a = "<br>"
        return mark_safe(a.join([ author.department for author in Author.objects.filter(thesis=obj.id) ]))

    def author_inline_city(self, obj):
        a = "<br>"
        return mark_safe(a.join([ author.city for author in Author.objects.filter(thesis=obj.id) ]))

    author_inline.short_description = "Авторы"
    author_inline_show.short_description = "Авторы тезиса"
    author_inline_status.short_description = "Статус авторов тезиса"
    author_inline_organization.short_description = "Организации авторов тезиса"
    author_inline_faculty.short_description = "Факультеты авторов тезиса"
    author_inline_department.short_description = "Депортаменты авторов тезиса"
    author_inline_city.short_description = "Города авторов тезиса"

    def download_thesis(self, request, queryset):
        """Выгрузить в excel"""
        response = HttpResponse(content_type='application/ms-excel')
        e = datetime.datetime.now()
        filename = "%s.%s.%s_%s:%s:%s_thesis.xls" % (e.day, e.month, e.year, e.hour, e.minute, e.second)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Thesis')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ["id", "Код рубрики", "Комментарий", "Номер секции", "Название доклада",  "Авторы тезиса",
                    "Контактное лицо", "Телефон", "Email", "Статус авторов", "Телефоны авторов", "Почты авторов",
                    "Организация", "Факультет", "Департамент", "Город",
                    "Научный руководитель", "Телефон научного руководителя", "Email научного руководителя",
                    "УМНИК", "Название проекта", "Цель выполнения НИР", "Назначение научно-технического продукта",
                    "Научная новизна предлагаемых в проекте решений", "Обоснование необходимости проведения НИР",
                    "Основные технические параметры, определяющие количественные, качественные и стоимостные характеристики продукции",
                    "Конструктивные требования", "Требования по патентной защите", "Область применения",
                    "Объем внебюджетных инвестиций или собственных средств",
                    "Имеющиеся аналоги", "План реализации"]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        font_style.num_format_str = '#,##0.00'


        rows = ThesisAll.objects.all().values_list("id", "code", "comment", "number", "title", "authors",
                    "cont_fio", "cont_phone_number", "cont_email","status", "phone_author", "email_authors",
                    "organization", "faculty", "department", "city",
                    "fio_dir", "phone_number_dir", "email_dir", "cleaver", "name_project", "aim", "purpose",
                    "novelty", "justification", "options", "requirements","protection", "application", "budget",
                    "analogue", "plan")
        for row in rows:
            print(row[0])
            if row[0] in list(queryset.values_list('id',flat=True)):
                row_num += 1
                for col_num in range(len(row)):
                    if col_num == 10:
                        ws.write(row_num, col_num, "'"+row[col_num], font_style)
                    else:
                        ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

    download_thesis.short_description = "Выгрузить в excel"
    download_thesis.allowed_permissions = ('change', )

    def scientific_director_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {} # sometimes context.copy() is better
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def scientific_director_inline_show(self, obj):
        return mark_safe(ScientificDirector.objects.get(thesis=obj.id).fio)

    scientific_director_inline.short_description = "Научный руководитель"
    scientific_director_inline_show.short_description = "Научный руководитель"

    fieldsets = (
     (None, {
        "fields": ("code", "sec_num", "comment", "title", "author_inline") # ключ  fields и кортеж тех полей, которые мы хотим использоват
     }),
     (None, {
            "fields": (("file1", "file2"), "scientific_director_inline")
     }),
     ('Контактные данные', {
            'fields': ("cont_fio", "cont_phone_number", "cont_email",),
     }),
     ('Участие в УМНИК', {
            'fields': ('cleaver',),
            'classes': ('predefined',)
     }),
    ("Умник", {
        "fields": ("name_project", "aim", "novelty", "justification", "options", "requirements",
                    "protection", "application", "budget", "analogue", "plan",),
        "classes": ('abcdefg',)
    })
    )

    form = ThesisForm

    class Media:
        js = ['thesis/js/base.js',]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Авторы тезисов"""
    list_display = ("fio_short", "fio", "date_birth", "status", "phone_number", "email", "organization", "faculty",
                    "department", "city", "thesis")
    list_display_links = ("fio_short",)


@admin.register(ScientificDirector)
class ScientificDirectorAdmin(admin.ModelAdmin):
    """Научные руководители"""
    list_display = ("fio", "phone_number", "email", "thesis")
    list_display_links = ("fio",)

admin.site.site_title = "Ежегодная межвузовская научно-техническая конференция студентов, аспирантов и молодых специалистов имени Е.В.Арменского"
admin.site.site_header = "Ежегодная межвузовская научно-техническая конференция студентов, аспирантов и молодых специалистов имени Е.В.Арменского"
