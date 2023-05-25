from django import forms
from .models import Resume


class ResumeCreationForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"


class ResumeChangeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"
