from django.db import transaction
from rest_framework import serializers

from .models import *


class SectionNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionNumber
        fields = '__all__'


class ScientificDirectorSerializer(serializers.ModelSerializer):
    thesis = serializers.PrimaryKeyRelatedField(queryset=Thesis.objects.all())
    class Meta:
        model = ScientificDirector
        fields = ["fio", "phone_number", "email", "thesis"]
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    thesis = serializers.PrimaryKeyRelatedField(queryset=Thesis.objects.all())
    class Meta:
        model = Author
        fields = ["fio_short", "fio", "date_birth", "status", "phone_number", "email", "organization", "faculty",
                  "department", "city", "thesis"]
        depth = 1


class ThesisWriteSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    director = ScientificDirectorSerializer(many=False)

    class Meta:
        model = Thesis
        fields = ["id", "code", "comment", "title", "sec_num",  'authors', "cont_fio", "cont_phone_number",
                  "cont_email", "director", "file1", "file2",
                  "cleaver", "name_project", "aim", "purpose", "novelty", "justification", "options",
                  "requirements", "protection", "application", "budget", "analogue", "plan", ]


class ThesisReadSerializer(serializers.ModelSerializer):
    sec_num = SectionNumberSerializer()

    class Meta(ThesisWriteSerializer.Meta):
        depth = 1
