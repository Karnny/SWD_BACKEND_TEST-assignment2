# serializers.py
from rest_framework import serializers
from apis.models import Personnel, StudentSubjectsScore, Classes, Schools

class PersonnelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'


class StudentSubjectsScoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectsScore
        fields = '__all__'


class ClassesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class SchoolsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'