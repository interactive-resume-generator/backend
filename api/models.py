from django.db import models
from django.contrib.auth import get_user_model


class Resume(models.Model):
    # owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    data = models.JSONField()
    format = models.JSONField()

    def __str__(self):
        return self.name

