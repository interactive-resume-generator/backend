from rest_framework import serializers
from .models import Resume, ResumeSection, SectionFormat


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'start')
        model = Resume


class ResumeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'type', 'next_section', 'section_format')
        model = ResumeSection


class SectionFormatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('type')
        model = SectionFormat

