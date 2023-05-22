from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Resume, ResumeSection, SectionFormat
from .serializer import ResumeSerializer, ResumeSectionSerializer, SectionFormatSerializer


class ResumeList(ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeSectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = ResumeSection.objects.all()
    serializer_class = ResumeSectionSerializer


class SectionFormatDetail(RetrieveUpdateDestroyAPIView):
    queryset = SectionFormat.objects.all()
    serializer_class = SectionFormatSerializer

