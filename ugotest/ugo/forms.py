from django import forms
# from django.forms import ModelForm
from ugo.models import Author, Category, Joke

class JokeForm(forms.ModelForm):
	author = forms.ModelChoiceField(queryset=Author.objects.all(), help_text="Author name", widget=forms.Select(attrs={'class': 'form-control'}))
	category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text="Choose category", widget=forms.Select(attrs={'class': 'form-control'}))
	joke = forms.CharField(max_length=200, help_text="Enter Joke", widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Joke
		fields = ('joke',)