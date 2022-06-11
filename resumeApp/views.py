from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'resumeApp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return redirect('/')

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'resumeApp/candidate.html', {'candidate':candidate})

