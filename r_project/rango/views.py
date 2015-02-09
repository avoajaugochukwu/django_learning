from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	context_dict = {'boldmessage': 'I am the new face of Django'}
	return render(request, 'rango/index.html', context_dict)

def about(request):
	return HttpResponse('This is the about page')