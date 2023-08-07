from rest_framework import serializers
from apis.models import StudentSubjectsScore

class StudentSubjectsScoreViewSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    subject_title = serializers.CharField()
    score = serializers.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = StudentSubjectsScore