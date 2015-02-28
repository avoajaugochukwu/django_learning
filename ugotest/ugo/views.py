from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ugo.models import Author, Joke
from ugo.forms import JokeForm



def index(request):
	context_dict = {'title': 'Jokes homepage'}

	jokes = Joke.objects.all()
	context_dict['jokes'] = jokes

	return render(request, 'ugo/index.html', context_dict)

def detail(request, qd):
	return HttpResponse('hello %s' %qd)


def authors(request, author_name):
	"""set title and header of page dynamically"""
	context_dict = {'title': author_name + ' page'}

	#get specific author instance
	author = Author.objects.get(name=author_name)

	#fetch all jokes by author - pass it to the dictionary
	jokes = Joke.objects.filter(author=author.id)
	context_dict['jokes'] = jokes

	return render(request, 'ugo/author.html', context_dict)




def add_joke(request):
	context_dict = {'name': 'Avoaja', 'title': 'Add Joke'}
	if request.method == 'POST':
		form = JokeForm(request.POST)
		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect('/ugo')
		else:
			print context_dict['form'].errors
	else:
		context_dict['form'] = JokeForm()
	return render(request, 'ugo/add_joke.html', context_dict)

