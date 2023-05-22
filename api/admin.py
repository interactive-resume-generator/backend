from django.contrib import admin
from .models import ResumeSection, Resume, SectionFormat

admin.site.register(Resume)
admin.site.register(ResumeSection)
admin.site.register(SectionFormat)