from django.db import models
from django.contrib.auth import get_user_model


class SectionFormat(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)
    type = models.TextField()


class ResumeSection(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.TextField()
    next_section = models.OneToOneField('self', on_delete=models.CASCADE, default=None, null=True, blank=True)
    section_format = models.ForeignKey(SectionFormat, on_delete=models.CASCADE)


class Resume(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start = models.ForeignKey(ResumeSection, on_delete=models.CASCADE)


