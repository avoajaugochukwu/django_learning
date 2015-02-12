from django import forms
from rango.models import Page, category

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='Please enter the category name')
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Category
		fields = ('name',)


class PageForm(forms.ModelForm):
	title = forms.CharField(max_length)
	url = forms.URLField(max_length=200, help_text='Please enter the category name')
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Page


		exclude = ('category',)
# li = [1, 2, 3, 4, 5]
# def ina(li):
# 	for x in li:
# 		yield x

# print ina(li)