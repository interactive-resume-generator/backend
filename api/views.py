from django.views import View
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
from .models import Resume
from .forms import ResumeCreationForm
from .serializer import ResumeSerializer


class ResumeList(ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeCreate(View):
    form_class = ResumeCreationForm

    def post(self, request, *args, **kwargs):
        print(request.body)
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            data = form.cleaned_data['data']
            resume_format = form.cleaned_data['format']

            model = Resume(name=name, data=data, format=resume_format)
            model.save()

            return JsonResponse({'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'})


