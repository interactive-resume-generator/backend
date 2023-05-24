from django.urls import path
from .views import ResumeList, ResumeDetail, ResumeCreate

urlpatterns = [
    path('', ResumeList.as_view(), name='resume_list'),
    path('<int:pk>', ResumeDetail.as_view(), name='resume_detail'),
    path('create/', ResumeCreate.as_view(), name='resume_create'),
]
