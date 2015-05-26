from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
	return HttpResponse('<h1>Your name is Ugochukwu</h1>')
