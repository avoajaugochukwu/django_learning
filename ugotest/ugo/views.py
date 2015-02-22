from django.shortcuts import render
from django.http import HttpResponse
from ugo.models import Author, Joke

# Create your views here.
def index(request):
	context_dict = {'title': 'Jokes homepage'}

	jokes = Joke.objects.all()
	context_dict['jokes'] = jokes

	return render(request, 'ugo/index.html', context_dict)

def detail(request, qd):
	return HttpResponse('hello %s' %qd)


def author(request, author_name):
	#set title and header of page dynamically - matches given author_name
	context_dict = {'title': author_name + ' page'}

	#get id of author
	author = Author.objects.get(name=author_name)

	#fetch all jokes by author - pass it to the dictionary
	context_dict['jokes'] = Joke.objects.filter(author=author.id)

	return render(request, 'ugo/author.html', context_dict)