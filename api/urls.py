from django.urls import path
from .views import ResumeList, ResumeDetail, ResumeSectionDetail, SectionFormatDetail

urlpatterns = [
    path('', ResumeList.as_view(), name='resume_list'),
    path('<int:pk>', ResumeDetail.as_view(), name='resume_detail'),
    path('section/<int:pk>', ResumeSectionDetail.as_view(), name='resume_section_detail'),
    path('sectionformat/<int:pk>', SectionFormatDetail.as_view(), name='section_format_detail')
]