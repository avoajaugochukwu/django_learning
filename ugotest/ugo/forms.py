from django import forms
from django.forms import ModelForm
from ugo.models import Author, Category, Joke

class JokeForm(forms.ModelForm):
	author = forms.ModelMultipleChoiceField(Author)
	category = forms.ModelChoiceField(Category)
	joke = forms.CharField(max_length=200)

	class Meta:
		model = Joke
		fields = ('joke',)