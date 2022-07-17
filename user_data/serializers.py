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
    #authors = AuthorSerializer(many=True)"director", 'authors'
    #director = ScientificDirectorSerializer(many=False)

    class Meta:
        model = Thesis
        fields = ["id", "code", "comment", "title", "sec_num", "file1", "file2", "cont_fio", "cont_phone_number",
                  "cont_email", "cleaver", "name_project", "aim", "purpose", "novelty", "justification", "options",
                  "requirements", "protection", "application", "budget", "analogue", "plan", ]

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('authors')
    #     director_data = validated_data.pop('director')
    #     thesis = Thesis.objects.create(**validated_data)
    #     for author in authors_data:
    #         a = Author.objects.create(**author, thesis=thesis)
    #         a.save()
    #     for dir in director_data:
    #         d = ScientificDirector.objects.create(**dir, thesis=thesis)
    #         d.save()
    #     return thesis

    # def update(self, instance, validated_data):
    #     lessons_data = validated_data.get('lesson_info')
    #     instance.save()
    # 
    #     for lesson_data in lessons_data:
    #         les_id = lesson_data.get('id_les', None)
    #         if les_id:
    #             lesson = Lessons.objects.get(id_les=les_id)
    #             lesson.name_les = lesson_data.get('name_les', lesson.name_les)
    #             lesson.lessonblock = lesson_data('lessonblock', instance.id_lb)
    #             lesson.video = lesson_data.get('video', lesson.video)
    #             lesson.video_st = lesson_data.get('video_st', lesson.video_st)
    #             lesson.lex_st = lesson_data.get('lex_st', lesson.lex_st)
    #             lesson.phr_st = lesson_data.get('phr_st', lesson.phr_st)
    #             lesson.dialog_st = lesson_data.get('dialog_st', lesson.dialog_st)
    #             lesson.rules_st = lesson_data.get('rules_st', lesson.rules_st)
    #             lesson.save()
    #         else:
    #             Lessons.objects.create(**lesson_data, lessonblock=instance)
    #     return instance


class ThesisReadSerializer(serializers.ModelSerializer):
    class Meta(ThesisWriteSerializer.Meta):
        depth = 1
