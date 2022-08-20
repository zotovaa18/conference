from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from rest_framework.decorators import schema

from .models import *
from .serializers import *

from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework import mixins
from django.views import View
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser

# Create your views here.


def BasePage(request):
    context = {}
    return render(request, 'base.html', context)


class SectionNumberList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает данные секции
     post:
       добавляет новую секцию
    """
    queryset = SectionNumber.objects.all()
    serializer_class = SectionNumberSerializer
    parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(operation_summary='получить список секций')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить новую секцию')
    def post(self, request):
        return self.create(request)


class SectionNumberDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретной секции
     put:
       изменяет данные в конкретной секции
     delete:
       удаляет данные о конкретной секции
    """
    queryset = SectionNumber.objects.all()
    serializer_class = SectionNumberSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной секции по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='получить список лексем', auto_schema=None)
    @schema(None)
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='получить список лексем', auto_schema=None)
    @schema(None)
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ScientificDirectorList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает данные о научных руководителях
     post:
       добавляет нового научного руководителя
    """
    queryset = ScientificDirector.objects.all()
    serializer_class = ScientificDirectorSerializer

    @swagger_auto_schema(operation_summary='получить список научных руководителей тезисов')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить нового научного руководителя тезиса')
    def post(self, request):
        return self.create(request)


class ScientificDirectorDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном научном руководителе
     put:
       изменяет данные о конкретном научном руководителе
     delete:
       удаляет данные о конкретном научном руководителе
    """
    queryset = ScientificDirector.objects.all()
    serializer_class = ScientificDirectorSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретной научном руководителе по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном научном руководителе')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном научном руководителе')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
    

class AuthorList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает данные о всех авторах тезиса
     post:
       добавляет нового автора тезиса
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @swagger_auto_schema(operation_summary='получить список авторов тезисов')
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(operation_summary='добавить нового автора тезиса')
    def post(self, request):
        return self.create(request)


class AuthorDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном авторе тезиса
     put:
       изменяет данные о конкретном авторе тезиса
     delete:
       удаляет данные о конкретном авторе тезиса
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном авторе тезиса по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные о конкретном авторе тезиса')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном авторе тезиса')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


class ThesisList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     get:
       возвращает данные о всех тезисах
     post:
       добавляет новый тезис
    """
    queryset = Thesis.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ThesisWriteSerializer
        else:
            return ThesisReadSerializer

    @swagger_auto_schema(operation_summary='получить список тезисов')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='добавить новый тезис', auto_schema=None)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ThesisDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
     get:
       возвращает данные о конкретном тезисе
     put:
       изменяет данные в конкретном тезисе
     delete:
       удаляет данные о конкретном тезисе
    """
    queryset = Thesis.objects.all()
    serializer_class = ThesisWriteSerializer

    @swagger_auto_schema(operation_summary='получить данные о конкретном тезисе по id')
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    @swagger_auto_schema(operation_summary='изменить данные в конкретном тезисе')
    def put(self, request, pk):
        return self.update(request, pk=pk)

    @swagger_auto_schema(operation_summary='удалить данные о конкретном тезисе')
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
