from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
	Functional test -> Test application from view/interest of User
	TDD -> Test application from view/interest of programmer
"""
def home_page(request):
	return HttpResponse('<html><title>To-Do lists</title></html>')
